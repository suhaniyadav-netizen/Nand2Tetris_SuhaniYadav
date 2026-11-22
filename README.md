# Nand2Tetris: From NAND to Modern Computer System

Building a general-purpose computer system from the ground up — starting from elementary logic gates and advancing through arithmetic logic, sequential memory, CPU architecture, assembly translation, and interactive low-level software.

---

### Student Information
- **Name:** Suhani Yadav  
- **Roll No:** 2501410032  
- **Repository:** [Nand2Tetris_SuhaniYadav](https://github.com/suhaniyadav-netizen/Nand2Tetris_SuhaniYadav)  

---

## Repository Structure

```plaintext
Nand2Tetris_SuhaniYadav/
├── Project 1/                                       # Elementary & Multi-bit Logic Gates
│   ├── And.hdl, Or.hdl, Not.hdl, Xor.hdl
│   ├── Mux.hdl, DMux.hdl
│   └── Not16.hdl, Mux4Way16.hdl, Mux8Way16.hdl
├── Project 2/                                       # Boolean Arithmetic & ALU
│   ├── HalfAdder.hdl, FullAdder.hdl, Add16.hdl
│   └── ALU.hdl
├── Project 3/                                       # Sequential Logic & Memory Hierarchy
│   ├── Bit.hdl, Register.hdl, PC.hdl
│   └── RAM8.hdl, RAM64.hdl, RAM512.hdl, RAM4K.hdl, RAM16K.hdl
├── Project 5/                                       # Computer Architecture
│   ├── Memory.hdl
│   ├── CPU.hdl
│   └── Computer.hdl
├── Lab 3 - CPU Architecture & Diagnostic Testing/   # Hack Assembly Diagnostic Programs
│   ├── add.asm
│   ├── branch.asm
│   └── loop.asm
├── SCREEN.asm and KBD.asm/                          # Memory-Mapped I/O Assembly
│   ├── SCREEN.asm
│   └── KBD.asm
├── capstone/                                        # Capstone System & Interactive Stack
│   ├── ALU.hdl, CPU.hdl, Memory.hdl, Computer.hdl
│   ├── assembler.py                                 # Two-Pass Python Hack Assembler
│   ├── Box.asm, Box.hack                            # Real-Time Interactive Application
│   ├── screenshots/                                 # Verification & Execution Records
│   └── README.md                                    # Comprehensive Capstone Documentation
└── README.md                                        # Master Repository Documentation
```

---

## Projects Overview

| Module | Category | Primary Components / Topics | Status | Directory Link |
| :--- | :--- | :--- | :--- | :--- |
| **Project 1** | Boolean Logic | Basic gates (`Nand` primitives), Multiplexers, Demultiplexers | Completed | [View Files](./Project%201) \| [GitHub](https://github.com/suhaniyadav-netizen/Nand2Tetris_SuhaniYadav/tree/main/Project%201) |
| **Project 2** | Boolean Arithmetic | Half/Full Adders, 16-bit Adder, Arithmetic Logic Unit (`ALU`) | Completed | [View Files](./Project%202) \| [GitHub](https://github.com/suhaniyadav-netizen/Nand2Tetris_SuhaniYadav/tree/main/Project%202) |
| **Project 3** | Sequential Logic | Flip-flops, Registers, Program Counter (`PC`), RAM hierarchy | Completed | [View Files](./Project%203) \| [GitHub](https://github.com/suhaniyadav-netizen/Nand2Tetris_SuhaniYadav/tree/main/Project%203) |
| **Project 5** | Architecture | Central Processing Unit (`CPU`), 32K `Memory`, `Computer` | Completed | [View Files](./Project%205) \| [GitHub](https://github.com/suhaniyadav-netizen/Nand2Tetris_SuhaniYadav/tree/main/Project%205) |
| **Lab 3** | CPU Diagnostics | Assembly testing: addition, conditional branching, loops | Completed | [View Files](./Lab%203%20-%20CPU%20Architecture%20%26%20Diagnostic%20Testing) \| [GitHub](https://github.com/suhaniyadav-netizen/Nand2Tetris_SuhaniYadav/tree/main/Lab%203%20-%20CPU%20Architecture%20%26%20Diagnostic%20Testing) |
| **I/O Assembly** | Memory-Mapped I/O | Direct pixel manipulation (`SCREEN`) and keyboard polling (`KBD`) | Completed | [View Files](./SCREEN.asm%20and%20KBD.asm) \| [GitHub](https://github.com/suhaniyadav-netizen/Nand2Tetris_SuhaniYadav/tree/main/SCREEN.asm%20and%20KBD.asm) |
| **Capstone** | Full-Stack Integration | Hardware integration, Two-pass Assembler, Interactive Box application | Completed | [View Files](./capstone) \| [Documentation](./capstone/README.md) \| [GitHub](https://github.com/suhaniyadav-netizen/Nand2Tetris_SuhaniYadav/tree/main/capstone) |

---

## Module Breakdown

### 1. Project 1: Boolean Logic
Explores combinational logic built entirely from fundamental `Nand` gates.
- **Elementary Logic Gates:**
  - [Not.hdl](file:///C:/Users/Suhani%20Yadav/OneDrive/Desktop/College/Nand2Tetris_SuhaniYadav/Project%201/Not.hdl), [And.hdl](file:///C:/Users/Suhani%20Yadav/OneDrive/Desktop/College/Nand2Tetris_SuhaniYadav/Project%201/And.hdl), [Or.hdl](file:///C:/Users/Suhani%20Yadav/OneDrive/Desktop/College/Nand2Tetris_SuhaniYadav/Project%201/Or.hdl), [Xor.hdl](file:///C:/Users/Suhani%20Yadav/OneDrive/Desktop/College/Nand2Tetris_SuhaniYadav/Project%201/Xor.hdl)
- **Selection & Routing Logic:**
  - [Mux.hdl](file:///C:/Users/Suhani%20Yadav/OneDrive/Desktop/College/Nand2Tetris_SuhaniYadav/Project%201/Mux.hdl), [DMux.hdl](file:///C:/Users/Suhani%20Yadav/OneDrive/Desktop/College/Nand2Tetris_SuhaniYadav/Project%201/DMux.hdl)
- **16-Bit & Multi-Way Buses:**
  - [Not16.hdl](file:///C:/Users/Suhani%20Yadav/OneDrive/Desktop/College/Nand2Tetris_SuhaniYadav/Project%201/Not16.hdl), [Mux4Way16.hdl](file:///C:/Users/Suhani%20Yadav/OneDrive/Desktop/College/Nand2Tetris_SuhaniYadav/Project%201/Mux4Way16.hdl), [Mux8Way16.hdl](file:///C:/Users/Suhani%20Yadav/OneDrive/Desktop/College/Nand2Tetris_SuhaniYadav/Project%201/Mux8Way16.hdl)

Local Folder: [Project 1/](file:///C:/Users/Suhani%20Yadav/OneDrive/Desktop/College/Nand2Tetris_SuhaniYadav/Project%201)

---

### 2. Project 2: Boolean Arithmetic & ALU
Constructs the computational core of the computer, culminating in the Hack Arithmetic Logic Unit.
- **Binary Adders:**
  - [HalfAdder.hdl](file:///C:/Users/Suhani%20Yadav/OneDrive/Desktop/College/Nand2Tetris_SuhaniYadav/Project%202/HalfAdder.hdl): Adds 2 single bits, producing sum and carry outputs.
  - [FullAdder.hdl](file:///C:/Users/Suhani%20Yadav/OneDrive/Desktop/College/Nand2Tetris_SuhaniYadav/Project%202/FullAdder.hdl): Adds 3 single bits including carry-in.
  - [Add16.hdl](file:///C:/Users/Suhani%20Yadav/OneDrive/Desktop/College/Nand2Tetris_SuhaniYadav/Project%202/Add16.hdl): 16-bit integer adder using carry-ripple architecture.
- **Arithmetic Logic Unit:**
  - [ALU.hdl](file:///C:/Users/Suhani%20Yadav/OneDrive/Desktop/College/Nand2Tetris_SuhaniYadav/Project%202/ALU.hdl): Computes 18 arithmetic/logical operations on two 16-bit registers controlled by 6 control bits (`zx, nx, zy, ny, f, no`), with zero (`zr`) and negative (`ng`) status flags.

Local Folder: [Project 2/](file:///C:/Users/Suhani%20Yadav/OneDrive/Desktop/College/Nand2Tetris_SuhaniYadav/Project%202)

---

### 3. Project 3: Sequential Logic & Memory Hierarchy
Introduces clocked storage elements built upon data flip-flops (DFF).
- **Registers & Counters:**
  - [Bit.hdl](file:///C:/Users/Suhani%20Yadav/OneDrive/Desktop/College/Nand2Tetris_SuhaniYadav/Project%203/Bit.hdl): 1-bit memory cell with load control.
  - [Register.hdl](file:///C:/Users/Suhani%20Yadav/OneDrive/Desktop/College/Nand2Tetris_SuhaniYadav/Project%203/Register.hdl): 16-bit data register.
  - [PC.hdl](file:///C:/Users/Suhani%20Yadav/OneDrive/Desktop/College/Nand2Tetris_SuhaniYadav/Project%203/PC.hdl): 16-bit Program Counter supporting reset, increment, and parallel load.
- **Hierarchical Random-Access Memory (RAM):**
  - [RAM8.hdl](file:///C:/Users/Suhani%20Yadav/OneDrive/Desktop/College/Nand2Tetris_SuhaniYadav/Project%203/RAM8.hdl) (8 registers)
  - [RAM64.hdl](file:///C:/Users/Suhani%20Yadav/OneDrive/Desktop/College/Nand2Tetris_SuhaniYadav/Project%203/RAM64.hdl) (64 registers)
  - [RAM512.hdl](file:///C:/Users/Suhani%20Yadav/OneDrive/Desktop/College/Nand2Tetris_SuhaniYadav/Project%203/RAM512.hdl) (512 registers)
  - [RAM4K.hdl](file:///C:/Users/Suhani%20Yadav/OneDrive/Desktop/College/Nand2Tetris_SuhaniYadav/Project%203/RAM4K.hdl) (4096 registers)
  - [RAM16K.hdl](file:///C:/Users/Suhani%20Yadav/OneDrive/Desktop/College/Nand2Tetris_SuhaniYadav/Project%203/RAM16K.hdl) (16384 registers)

Local Folder: [Project 3/](file:///C:/Users/Suhani%20Yadav/OneDrive/Desktop/College/Nand2Tetris_SuhaniYadav/Project%203)

---

### 4. Project 5: Computer Architecture
Integrates the complete microarchitecture according to the Von Neumann model.
- [Memory.hdl](file:///C:/Users/Suhani%20Yadav/OneDrive/Desktop/College/Nand2Tetris_SuhaniYadav/Project%205/Memory.hdl): Unified 32K memory mapping:
  - `0x0000 - 0x3FFF`: 16K Data RAM
  - `0x4000 - 0x5FFF`: 8K Screen memory map
  - `0x6000`: Keyboard scan code register
- [CPU.hdl](file:///C:/Users/Suhani%20Yadav/OneDrive/Desktop/College/Nand2Tetris_SuhaniYadav/Project%205/CPU.hdl): Central Processing Unit decoding A/C instructions, register routing (`A`, `D`), condition evaluations, and program flow control.
- [Computer.hdl](file:///C:/Users/Suhani%20Yadav/OneDrive/Desktop/College/Nand2Tetris_SuhaniYadav/Project%205/Computer.hdl): Top-level chip tying CPU, Memory, and `ROM32K` together.

Local Folder: [Project 5/](file:///C:/Users/Suhani%20Yadav/OneDrive/Desktop/College/Nand2Tetris_SuhaniYadav/Project%205)

---

### 5. Assembly Diagnostics & Peripheral I/O
Low-level assembly programs written in the Hack instruction set to verify processor behavior and peripheral interfacing.
- **CPU Diagnostics ([Lab 3 - CPU Architecture & Diagnostic Testing/](file:///C:/Users/Suhani%20Yadav/OneDrive/Desktop/College/Nand2Tetris_SuhaniYadav/Lab%203%20-%20CPU%20Architecture%20%26%20Diagnostic%20Testing)):**
  - [add.asm](file:///C:/Users/Suhani%20Yadav/OneDrive/Desktop/College/Nand2Tetris_SuhaniYadav/Lab%203%20-%20CPU%20Architecture%20%26%20Diagnostic%20Testing/add.asm): Verifies addition: computes `RAM[2] = RAM[0] + RAM[1]`.
  - [branch.asm](file:///C:/Users/Suhani%20Yadav/OneDrive/Desktop/College/Nand2Tetris_SuhaniYadav/Lab%203%20-%20CPU%20Architecture%20%26%20Diagnostic%20Testing/branch.asm): Verifies conditional branching: compares `RAM[0]` and `RAM[1]`, assigning `RAM[2] = 1` if `R0 > R1`, else `0`.
  - [loop.asm](file:///C:/Users/Suhani%20Yadav/OneDrive/Desktop/College/Nand2Tetris_SuhaniYadav/Lab%203%20-%20CPU%20Architecture%20%26%20Diagnostic%20Testing/loop.asm): Verifies iterative execution: sums numbers from 1 to 5 into `RAM[1]`.
- **Memory-Mapped I/O ([SCREEN.asm and KBD.asm/](file:///C:/Users/Suhani%20Yadav/OneDrive/Desktop/College/Nand2Tetris_SuhaniYadav/SCREEN.asm%20and%20KBD.asm)):**
  - [SCREEN.asm](file:///C:/Users/Suhani%20Yadav/OneDrive/Desktop/College/Nand2Tetris_SuhaniYadav/SCREEN.asm%20and%20KBD.asm/SCREEN.asm): Directly accesses addresses `16384`, `16416`, `16448`, and `16480`, illuminating vertical lines on the display.
  - [KBD.asm](file:///C:/Users/Suhani%20Yadav/OneDrive/Desktop/College/Nand2Tetris_SuhaniYadav/SCREEN.asm%20and%20KBD.asm/KBD.asm): Continuously polls `KBD` (`RAM[24576]`) waiting for the ASCII key code `113` ('q') to terminate execution.

---

### 6. Capstone Project
The culmination of the Nand2Tetris curriculum, synthesizing microarchitecture design, systems software, and interactive application engineering.

- **Microarchitecture Stack:** [ALU.hdl](file:///C:/Users/Suhani%20Yadav/OneDrive/Desktop/College/Nand2Tetris_SuhaniYadav/capstone/ALU.hdl), [CPU.hdl](file:///C:/Users/Suhani%20Yadav/OneDrive/Desktop/College/Nand2Tetris_SuhaniYadav/capstone/CPU.hdl), [Memory.hdl](file:///C:/Users/Suhani%20Yadav/OneDrive/Desktop/College/Nand2Tetris_SuhaniYadav/capstone/Memory.hdl), and [Computer.hdl](file:///C:/Users/Suhani%20Yadav/OneDrive/Desktop/College/Nand2Tetris_SuhaniYadav/capstone/Computer.hdl).
- **Two-Pass Python Assembler ([assembler.py](file:///C:/Users/Suhani%20Yadav/OneDrive/Desktop/College/Nand2Tetris_SuhaniYadav/capstone/assembler.py)):**
  Translates Hack assembly into 16-bit machine code with symbol resolution and personalized duplicate label detection ($K = 32 \implies 32 \bmod 3 = 2$).
- **Interactive Box Program ([Box.asm](file:///C:/Users/Suhani%20Yadav/OneDrive/Desktop/College/Nand2Tetris_SuhaniYadav/capstone/Box.asm) / [Box.hack](file:///C:/Users/Suhani%20Yadav/OneDrive/Desktop/College/Nand2Tetris_SuhaniYadav/capstone/Box.hack)):**
  Calibrated for $K = 32$ (Row 32, Offset 1024 words, Start Address 17408, Size $16 \times 20$ pixels). Utilizes differential state-tracking (`last_color`) for instant, flicker-free keyboard interaction.
- **Verification Records:** Comprehensive test runs ([screenshots/](file:///C:/Users/Suhani%20Yadav/OneDrive/Desktop/College/Nand2Tetris_SuhaniYadav/capstone/screenshots)) verifying CPU, Memory, Computer benchmarks (`Add`, `Max`, `Rect`), and interactive application states.

Detailed documentation: [capstone/README.md](file:///C:/Users/Suhani%20Yadav/OneDrive/Desktop/College/Nand2Tetris_SuhaniYadav/capstone/README.md)

---

## Tooling & Simulation

- **Hardware Simulator:** Used for unit testing individual `.hdl` gate designs and chip implementations against `.tst` test scripts.
- **CPU Emulator:** Used for executing compiled `.hack` binaries and running interactive memory-mapped I/O programs.
- **Python Runtime:** Python 3 execution environment for the two-pass Hack assembler (`assembler.py`).
- **Official Nand2Tetris Web IDE:** [Nand2Tetris Chip IDE](https://nand2tetris.github.io/web-ide/chip/)
