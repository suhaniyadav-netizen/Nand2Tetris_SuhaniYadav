# Two-Pass Hack Assembler with Duplicate Label Warning (K = 32 -> 32 mod 3 = 2)

import sys
import os

# Predefined Hack symbols
PREDEFINED_SYMBOLS = {
    "R0": 0, "R1": 1, "R2": 2, "R3": 3,
    "R4": 4, "R5": 5, "R6": 6, "R7": 7,
    "R8": 8, "R9": 9, "R10": 10, "R11": 11,
    "R12": 12, "R13": 13, "R14": 14, "R15": 15,
    "SP": 0, "LCL": 1, "ARG": 2, "THIS": 3, "THAT": 4,
    "SCREEN": 16384, "KBD": 24576
}

# C-instruction computation lookup table (a + c1..c6 = 7 bits)
COMP_TABLE = {
    # a = 0 (uses A register)
    "0":   "0101010",
    "1":   "0111111",
    "-1":  "0111010",
    "D":   "0001100",
    "A":   "0110000",
    "!D":  "0001101",
    "!A":  "0110001",
    "-D":  "0001111",
    "-A":  "0110011",
    "D+1": "0011111",
    "A+1": "0110111",
    "D-1": "0001110",
    "A-1": "0110010",
    "D+A": "0000010",
    "A+D": "0000010",
    "D-A": "0010011",
    "A-D": "0000111",
    "D&A": "0000000",
    "A&D": "0000000",
    "D|A": "0010101",
    "A|D": "0010101",

    # a = 1 (uses M = RAM[A])
    "M":   "1110000",
    "!M":  "1110001",
    "-M":  "1110011",
    "M+1": "1110111",
    "M-1": "1110010",
    "D+M": "1000010",
    "M+D": "1000010",
    "D-M": "1010011",
    "M-D": "1000111",
    "D&M": "1000000",
    "M&D": "1000000",
    "D|M": "1010101",
    "M|D": "1010101",
}

# C-instruction destination lookup table (d1 d2 d3 = A D M)
DEST_TABLE = {
    None:  "000",
    "":    "000",
    "M":   "001",
    "D":   "010",
    "MD":  "011",
    "DM":  "011",
    "A":   "100",
    "AM":  "101",
    "MA":  "101",
    "AD":  "110",
    "DA":  "110",
    "AMD": "111",
    "ADM": "111",
}

# C-instruction jump lookup table (j1 j2 j3 = <0 ==0 >0)
JUMP_TABLE = {
    None:  "000",
    "":    "000",
    "JGT": "001",
    "JEQ": "010",
    "JGE": "011",
    "JLT": "100",
    "JNE": "101",
    "JLE": "110",
    "JMP": "111",
}


def clean_line(raw_line: str) -> str:
    """Remove inline comments and all whitespace from a line."""
    no_comment = raw_line.split("//")[0]
    return "".join(no_comment.split())


def first_pass(lines: list[str], symbol_table: dict[str, int]) -> list[str]:
    """
    Pass 1:
    - Strip comments and blank lines.
    - Record label declarations (LABEL) with their ROM instruction address.
    - Print a warning if a duplicate label is declared (Personalized Feature: K=32).
    - Return a list of cleaned real instructions (A- and C-instructions).
    """
    cleaned_instructions = []
    declared_labels = set()
    rom_address = 0

    for line_num, raw_line in enumerate(lines, start=1):
        instruction = clean_line(raw_line)
        if not instruction:
            continue

        # Check for label pseudo-instruction: (LABEL_NAME)
        if instruction.startswith("(") and instruction.endswith(")"):
            label = instruction[1:-1]
            if label in declared_labels:
                print(f"WARNING (Line {line_num}): Duplicate label '({label})' declared. Keeping first definition at ROM address {symbol_table[label]}.")
            else:
                declared_labels.add(label)
                symbol_table[label] = rom_address
        else:
            cleaned_instructions.append(instruction)
            rom_address += 1

    return cleaned_instructions


def translate_a_instruction(instruction: str, symbol_table: dict[str, int], next_ram_address: int) -> tuple[str, int]:
    """Translate @value or @symbol into a 16-bit binary string."""
    symbol = instruction[1:]

    if symbol.isdigit():
        address = int(symbol)
    else:
        if symbol not in symbol_table:
            symbol_table[symbol] = next_ram_address
            next_ram_address += 1
        address = symbol_table[symbol]

    # Format as 16-bit binary (leading 0 + 15-bit address)
    binary_code = f"0{address:015b}"
    return binary_code, next_ram_address


def translate_c_instruction(instruction: str) -> str:
    """Translate dest=comp;jump into a 16-bit binary string."""
    dest = None
    jump = None
    comp_part = instruction

    # Split jump if ';' is present
    if ";" in comp_part:
        comp_part, jump = comp_part.split(";", 1)

    # Split dest if '=' is present
    if "=" in comp_part:
        dest, comp = comp_part.split("=", 1)
    else:
        comp = comp_part

    if comp not in COMP_TABLE:
        raise ValueError(f"Invalid comp mnemonic '{comp}' in instruction '{instruction}'")
    if dest not in DEST_TABLE:
        raise ValueError(f"Invalid dest mnemonic '{dest}' in instruction '{instruction}'")
    if jump not in JUMP_TABLE:
        raise ValueError(f"Invalid jump mnemonic '{jump}' in instruction '{instruction}'")

    return "111" + COMP_TABLE[comp] + DEST_TABLE[dest] + JUMP_TABLE[jump]


def second_pass(instructions: list[str], symbol_table: dict[str, int]) -> list[str]:
    """
    Pass 2:
    - Convert every cleaned A- and C-instruction into 16-bit binary machine code.
    - Allocate new variables starting at RAM address 16.
    """
    machine_code = []
    next_ram_address = 16

    for instruction in instructions:
        if instruction.startswith("@"):
            binary_line, next_ram_address = translate_a_instruction(
                instruction, symbol_table, next_ram_address
            )
        else:
            binary_line = translate_c_instruction(instruction)

        machine_code.append(binary_line)

    return machine_code


def assemble_file(asm_path: str) -> str:
    """Read an .asm file, run two-pass assembly, and write the .hack file."""
    if not os.path.isfile(asm_path):
        raise FileNotFoundError(f"Input file not found: {asm_path}")

    with open(asm_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    # Copy predefined symbols so each assembly run starts fresh
    symbol_table = dict(PREDEFINED_SYMBOLS)

    # Pass 1: Collect labels & warn on duplicates
    cleaned_instructions = first_pass(lines, symbol_table)

    # Pass 2: Generate 16-bit binary code
    binary_lines = second_pass(cleaned_instructions, symbol_table)

    # Write output .hack file next to input .asm file
    base_name, _ = os.path.splitext(asm_path)
    hack_path = base_name + ".hack"

    with open(hack_path, "w", encoding="utf-8") as f:
        for line in binary_lines:
            f.write(line + "\n")

    print(f"Assembled '{asm_path}' -> '{hack_path}' ({len(binary_lines)} instructions)")
    return hack_path


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python assembler.py <path/to/program.asm>")
        sys.exit(1)

    assemble_file(sys.argv[1])