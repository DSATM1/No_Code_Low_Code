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



Line-by-Line Explanation
Step 1: Handle Edge Cases
if numRows == 1 or numRows >= len(s):
    return s
If there's only one row, no zigzag is needed.
If the number of rows is greater than or equal to the string length, each character stays in its own row.
Step 2: Create Rows
rows = [""] * numRows

For numRows = 3:

[
 "",
 "",
 ""
]

Each element stores characters for one row.

Step 3: Initialize Variables
current_row = 0
direction = 1
current_row keeps track of the current row.
direction = 1 means moving down.
direction = -1 means moving up.
Step 4: Traverse the String
for char in s:

Process one character at a time.

Step 5: Add Character to Current Row
rows[current_row] += char

Example:

Row 0: P
Row 1: A
Row 2: Y
Step 6: Change Direction
if current_row == 0:
    direction = 1

elif current_row == numRows - 1:
    direction = -1
At the top row, start moving down.
At the bottom row, start moving up.
Step 7: Move to Next Row
current_row += direction

Update the row index based on the current direction.

Step 8: Return the Result
return "".join(rows)

Combine all rows into the final string.

Dry Run

Input:

s = "PAYPALISHIRING"
numRows = 3
Character	Row	    Rows After Insertion
P	        0	    P
A	        1	    P / A
Y	        2	    P / A / Y
P	        1	    P / AP / Y
A	        0	    PA / AP / Y
L	        1	    PA / APL / Y
I	        2	    PA / APL / YI
S	        1	    PA / APLS / YI
H	        0	    PAH / APLS / YI
I	        1	    PAH / APLSI / YI
R	        2	    PAH / APLSI / YIR
I	        1	    PAH / APLSII / YIR
N	        0	    PAHN / APLSII / YIR
G	        1	    PAHN / APLSIIG / YIR

Final answer:

PAHNAPLSIIGYIR

Complexity Analysis
Complexity	Value
Time	O(n)
Space	O(n)
Each character is processed exactly once.
The extra space is used to store the rows.


Pattern Used

This problem demonstrates a Simulation pattern:

Simulate moving through rows in a zigzag.
Use a direction flag (down/up) to control movement.
Build the result incrementally.

This type of row-by-row simulation is a common interview pattern for string manipulation problems.
