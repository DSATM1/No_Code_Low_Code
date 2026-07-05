LeetCode #7 – Reverse Integer

Difficulty: Medium

Problem Statement

Given a signed 32-bit integer x, return x with its digits reversed.

If reversing x causes the value to go outside the signed 32-bit integer range:

[-2^31, 2^31 - 1]

return 0.

Note: You cannot use 64-bit integers to store the reversed number.

Example 1
Input:
x = 123

Output:
321

Example 2
Input:
x = -123

Output:
-321

Example 3
Input:
x = 120

Output:
21

Example 4
Input:
x = 1534236469

Output:
0

Explanation:

9646324351

This exceeds the 32-bit signed integer limit, so return 0.

Approach 1: String Reversal (Easy to Understand)
Idea
1. Convert the integer to a string.
2. Reverse the string.
3. Convert it back to an integer.
4. Restore the sign.
5. Check for 32-bit overflow.

Python Code
  
class Solution:
    def reverse(self, x: int) -> int:

        sign = -1 if x < 0 else 1

        x = abs(x)

        reversed_num = int(str(x)[::-1])

        reversed_num *= sign

        if reversed_num < -2**31 or reversed_num > 2**31 - 1:
            return 0

        return reversed_num


Time Complexity
O(n)

where n is the number of digits.

Space:
O(n)

Approach 2: Mathematical Reversal (Interview Preferred)

Instead of converting to a string, reverse the number digit by digit.

Idea

Take the last digit using % 10.

Remove the last digit using // 10.

Build the reversed number.

Example

Input:

123
Step 1
digit = 3

reverse = 3

remaining = 12

Step 2
digit = 2

reverse = 32

remaining = 1

Step 3
digit = 1

reverse = 321

remaining = 0

Answer:

321
