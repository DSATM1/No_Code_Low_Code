
LeetCode #12 – Integer to Roman

Difficulty: Medium

Roman Numeral Rules
1. Basic Symbols
I = 1
V = 5
X = 10
L = 50
C = 100
D = 500
M = 1000
2. Repeating Symbols

Some symbols can be repeated up to three times:

III = 3
XXX = 30
CCC = 300
MMM = 3000
3. Subtractive Notation

Instead of writing four identical symbols, Roman numerals use subtraction.

Number	Roman
4	      IV
9	      IX
40	    XL
90	    XC
400	    CD
900	    CM



Example 1
Input:
num = 3

Output:
"III"
Example 2
Input:
num = 58

Output:
"LVIII"

Explanation:

50 = L

5 = V

3 = III

Answer = LVIII
Example 3
Input:
num = 1994

Output:
"MCMXCIV"

Explanation:

1000 = M

900 = CM

90 = XC

4 = IV

Answer = MCMXCIV



Approach (Greedy Algorithm)
Idea

Always use the largest Roman numeral value that is less than or equal to the current number.

Subtract that value and continue until the number becomes 0.

Roman Value Table
values = [
    (1000, "M"),
    (900, "CM"),
    (500, "D"),
    (400, "CD"),
    (100, "C"),
    (90, "XC"),
    (50, "L"),
    (40, "XL"),
    (10, "X"),
    (9, "IX"),
    (5, "V"),
    (4, "IV"),
    (1, "I")
]

Notice that the subtractive values (900, 400, 90, etc.) are included explicitly.
