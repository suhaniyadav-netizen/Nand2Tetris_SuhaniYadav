// Roll No: 2501410032, K = 32
// Description:
// Displays 16x20 black rectangle starting at row 32 on left edge whenever any key is pressed, and clears it when key is released.
// Memory Calculations (K = 32):
//   SCREEN base address = 16384
//   Starting row        = 32  -> offset = 32 * 32 = 1024
//   Start address       = 16384 + 1024 = 17408
//   Height              = 20 rows (rows 32 to 51)
//   Width               = 16 * ((32 mod 4) + 1) = 16 pixels (1 word per row)

(MAIN_LOOP)
    // 1. Check keyboard memory map (RAM[24576])
    @KBD
    D=M                 // D = ASCII code of pressed key (0 if none)

    @SET_BLACK
    D;JNE               // If any key is pressed (D != 0), set color to black (-1)

    // No key pressed -> set color = 0 (white)
    @color
    M=0
    @START_DRAW
    0;JMP

(SET_BLACK)
    // Key pressed -> set color = -1 (16 black pixels: 1111111111111111)
    @color
    M=-1

(START_DRAW)
    // 2. Initialize starting screen address: 16384 + (32 * 32) = 17408
    @17408
    D=A
    @addr
    M=D                 // addr = 17408 (row 32, left edge)

    // 3. Initialize row counter = 20 rows
    @20
    D=A
    @rows_left
    M=D                 // rows_left = 20

(DRAW_LOOP)
    // Load current color (-1 for black, 0 for white)
    @color
    D=M

    // Write color to current 16-pixel screen word
    @addr
    A=M                 // Set A-register to target screen address
    M=D                 // Draw 16 black or white pixels

    // Move down 1 row (each row is 32 words wide)
    @addr
    D=M
    @32
    D=D+A
    @addr
    M=D                 // addr = addr + 32

    // Decrement row counter and repeat until all 20 rows are drawn
    @rows_left
    MD=M-1
    @DRAW_LOOP
    D;JGT               // Continue if rows_left > 0

    // Finished all 20 rows -> poll keyboard again
    @MAIN_LOOP
    0;JMP