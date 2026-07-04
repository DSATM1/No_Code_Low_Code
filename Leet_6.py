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
