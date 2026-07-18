
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


Algorithm
Store Roman values from largest to smallest.
Initialize an empty result string.
Traverse the list of values.
While the current value is less than or equal to num:
Append the Roman symbol.
Subtract the value from num.
Return the result.


Python Code
class Solution:
    def intToRoman(self, num: int) -> str:

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

        result = ""

        for value, symbol in values:

            while num >= value:

                result += symbol
                num -= value

        return result




Line-by-Line Explanation
Step 1: Roman Value Mapping
values = [
    (1000, "M"),
    (900, "CM"),
    ...
]

Store all Roman numeral values in descending order.

Step 2: Result String
result = ""

This string will store the final Roman numeral.

Step 3: Traverse the Values
for value, symbol in values:

Check each Roman numeral from largest to smallest.

Step 4: Use the Largest Possible Value
while num >= value:

If the current value fits into num, use it.

Example:

num = 58

58 >= 50 ✔

Append "L" and subtract 50.

Remaining:

8
Step 5: Append the Symbol
result += symbol

Example:

Result = "L"
Step 6: Subtract the Value
num -= value

Example:

58 - 50 = 8

Continue until num becomes 0.

Step 7: Return the Result
return result



Dry Run
Input
num = 1994
Value	Symbol	Remaining num	Result
1000	M	    994	            M
900	    CM	    94	            MCM
90	    XC	    4	            MCMXC
4	    IV	    0	            MCMXCIV

Final answer:

MCMXCIV
Another Example

Input:

num = 3749

Steps:

3749

3000 → MMM

700 → DCC

40 → XL

9 → IX

Result:

MMMDCCXLIX
Complexity Analysis
Complexity	Value
Time	O(1)
Space	O(1)
Why O(1)?
The Roman value table always contains 13 entries.
The input range is limited to 1–3999.
Therefore, the algorithm performs a constant amount of work regardless of the input size.
Pattern Used

This problem uses the Greedy Algorithm pattern.

Why Greedy?

At every step, we make the locally optimal choice:

Pick the largest Roman value that does not exceed the remaining number.

This strategy always leads to the correct Roman numeral because Roman numerals are built from the largest possible symbols first.

Similar Greedy Problems
LeetCode #13 – Roman to Integer
LeetCode #45 – Jump Game II
LeetCode #55 – Jump Game
LeetCode #134 – Gas Station
LeetCode #435 – Non-overlapping Intervals

Interview Tip: A good clue that a greedy approach may work is when making the best local choice repeatedly leads to the correct global solution, as it does with Roman numeral conversion.
