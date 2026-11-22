// File name: capstone/Box.asm
// Author: Suhani Yadav (Roll No: 2501410032, K = 32)
// Description:
//   Displays a 16x20 black rectangle starting at row 32 on the left edge
//   whenever any key is pressed, and clears it immediately when released.
//   Uses state tracking (last_color) so keyboard polling is instantaneous.
//
// Memory Calculations (K = 32):
//   SCREEN base address = 16384
//   Starting row        = 32  -> offset = 32 * 32 = 1024
//   Start address       = 16384 + 1024 = 17408
//   Height              = 20 rows (rows 32 to 51)
//   Width               = 16 * ((32 mod 4) + 1) = 16 pixels (1 word per row)

    // Initialize last_color = 0 (screen starts white)
    @last_color
    M=0

(MAIN_LOOP)
    // 1. Poll keyboard memory map (RAM[24576])
    @KBD
    D=M                 // D = ASCII code of pressed key (0 if none)

    @SET_BLACK
    D;JNE               // If any key is pressed (D != 0), target color = -1

    // No key pressed -> target color = 0 (white)
    @color
    M=0
    @CHECK_CHANGE
    0;JMP

(SET_BLACK)
    // Key pressed -> target color = -1 (16 black pixels)
    @color
    M=-1

(CHECK_CHANGE)
    // 2. Only redraw the 20 rows if color changed since last frame
    @color
    D=M
    @last_color
    D=D-M               // D = color - last_color
    @MAIN_LOOP
    D;JEQ               // If unchanged, skip drawing and keep polling KBD immediately!

    // Update last_color = color
    @color
    D=M
    @last_color
    M=D

    // 3. Initialize starting screen address: 16384 + (32 * 32) = 17408
    @17408
    D=A
    @addr
    M=D                 // addr = 17408 (row 32, left edge)

    // 4. Initialize row counter = 20 rows
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
    A=M
    M=D

    // Move down 1 row (each row is 32 words wide)
    @addr
    D=M
    @32
    D=D+A
    @addr
    M=D

    // Decrement row counter and repeat until all 20 rows are drawn
    @rows_left
    MD=M-1
    @DRAW_LOOP
    D;JGT

    // Return to fast keyboard polling
    @MAIN_LOOP
    0;JMP