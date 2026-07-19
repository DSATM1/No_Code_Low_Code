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


Approach (Greedy Traversal)
Key Idea

Traverse the string from left to right.

For each character:

If its value is less than the next character's value, subtract it.
Otherwise, add it.
Roman Value Dictionary
roman = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}
Algorithm
Create a dictionary of Roman values.
Initialize total = 0.
Traverse the string.
If the current value is less than the next value:
Subtract it.
Otherwise:
Add it.
Return the total.
Python Code


class Solution:
    def romanToInt(self, s: str) -> int:

        roman = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        total = 0

        for i in range(len(s)):

            if i < len(s) - 1 and roman[s[i]] < roman[s[i + 1]]:
                total -= roman[s[i]]
            else:
                total += roman[s[i]]

        return total


Line-by-Line Explanation
Step 1: Create Dictionary
roman = {
    "I":1,
    "V":5,
    "X":10,
    "L":50,
    "C":100,
    "D":500,
    "M":1000
}

This allows quick lookup of each Roman numeral's value.

Step 2: Initialize Total
total = 0

This variable stores the final integer.

Step 3: Traverse the String
for i in range(len(s)):

Process each Roman numeral character.

Step 4: Check for Subtraction
if i < len(s) - 1 and roman[s[i]] < roman[s[i + 1]]:

Example:

IV

1 < 5

Subtract 1.

Step 5: Add Otherwise
else:
    total += roman[s[i]]

Example:

VI

5 > 1

Add both.
Step 6: Return Result
return total
Dry Run
Input
s = "MCMXCIV"
