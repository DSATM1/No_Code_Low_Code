
LeetCode #9 – Palindrome Number

Difficulty: Easy

Problem Statement

Given an integer x, return True if x is a palindrome, and False otherwise.

A palindrome reads the same forward and backward.

Example 1
Input:
x = 121

Output:
True

Explanation:

121 → 121

Example 2
Input:
x = -121

Output:
False

Explanation:

Forward  : -121
Backward : 121-

They are not the same.


Example 3
Input:
x = 10

Output:
False

Explanation:

Forward  : 10
Backward : 01


Approach 1: Convert to String (Easy)
Idea

Convert the number to a string and compare it with its reverse.

Python Code

class Solution:
    def isPalindrome(self, x: int) -> bool:

        return str(x) == str(x)[::-1]

Time Complexity
O(n)
Space Complexity
O(n)

where n is the number of digits.

Approach 2: Reverse the Integer (Interview Preferred)
Idea

Reverse the number mathematically and compare it with the original.

Algorithm
Negative numbers are never palindromes.
Save the original number.
Reverse the digits one by one.
Compare the reversed number with the original.

    
Python Code

class Solution:
    def isPalindrome(self, x: int) -> bool:

        if x < 0:
            return False

        original = x
        reverse = 0

        while x > 0:

            digit = x % 10

            reverse = reverse * 10 + digit

            x //= 10

        return original == reverse
