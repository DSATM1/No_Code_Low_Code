LeetCode #6 – Zigzag Conversion

Difficulty: Medium


Problem Statement

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows.

For example, with 3 rows:

P   A   H   N
A P L S I I G
Y   I   R

Reading row by row gives:

PAHNAPLSIIGYIR

Write a function that converts a string into this zigzag format.

Example 1
Input:
s = "PAYPALISHIRING"
numRows = 3

Output:
"PAHNAPLSIIGYIR"

Example 2
Input:
s = "PAYPALISHIRING"
numRows = 4

Output:
"PINALSIGYAHRPI"

Zigzag:

P     I     N
A   L S   I G
Y A   H R
P     I
Example 3
Input:
s = "A"
numRows = 1

Output:
"A"

Approach 1: Simulate the Zigzag (Optimal)
Idea

Create a list for each row.

Move down through the rows, then up diagonally, repeating until all characters are placed.

Finally, join all rows together.

Visualization

Input:

s = "PAYPALISHIRING"
numRows = 3

Start:

Row 0:
Row 1:
Row 2:

Add characters one by one:

Row 0: P
Row 1: A
Row 2: Y

Move upward:

Row 0: PA
Row 1: AP
Row 2: Y

Continue:

Row 0: PAHN
Row 1: APLSIIG
Row 2: YIR

Join all rows:

PAHNAPLSIIGYIR

Algorithm
1. If numRows == 1 or numRows >= len(s), return s.
2. Create a list of empty strings (one for each row).
3. Start at row 0.
4. Move downward until the last row.
5. Reverse direction and move upward.
6. Append each character to the current row.
7. Join all rows.

Python Code

class Solution:
    def convert(self, s: str, numRows: int) -> str:

        if numRows == 1 or numRows >= len(s):
            return s

        rows = [""] * numRows

        current_row = 0
        direction = 1

        for char in s:

            rows[current_row] += char

            if current_row == 0:
                direction = 1

            elif current_row == numRows - 1:
                direction = -1

            current_row += direction

        return "".join(rows)
