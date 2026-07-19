LeetCode #13 – Roman to Integer

Difficulty: Easy
Problem Statement

Roman numerals are represented by seven symbols:

Symbol	Value
I	      1
V	      5
X	      10
L	      50
C	      100
D	      500
M	      1000

Given a Roman numeral string s, convert it to an integer.

Constraints:

1 <= s.length <= 15
s is a valid Roman numeral.


Roman Numeral Rules
Normal Addition

If a symbol is greater than or equal to the next symbol, add its value.

Example:

VIII

5 + 1 + 1 + 1 = 8
Subtractive Notation

If a smaller value comes before a larger value, subtract it.

Examples:

Roman	Integer
IV	  4
IX	  9
XL	  40
XC	  90
CD	  400
CM	  900


Example 1
Input:
s = "III"

Output:
3
Example 2
Input:
s = "LVIII"

Output:
58

Explanation:

L = 50

V = 5

III = 3

Total = 58
Example 3
Input:
s = "MCMXCIV"

Output:
1994

Explanation:

M  = 1000

CM = 900

XC = 90

IV = 4

Total = 1994
