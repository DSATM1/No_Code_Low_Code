
LeetCode #17 – Letter Combinations of a Phone Number

Difficulty: Medium

Problem Statement

Given a string digits containing digits from 2–9, return all possible letter combinations that the number could represent.

The mapping is the same as on a telephone keypad.

Return the answer in any order.
Phone Keypad Mapping
Digit	Letters
2	    abc
3	    def
4	    ghi
5	    jkl
6	    mno
7	    pqrs
8	    tuv
9	    wxyz


Example 1
Input:
digits = "23"

Output:
[
"ad","ae","af",
"bd","be","bf",
"cd","ce","cf"
]
Example 2
Input:
digits = ""

Output:
[]
Example 3
Input:
digits = "2"

Output:
["a","b","c"]


Approach: Backtracking (Optimal)
Key Idea

Each digit has multiple possible letters.

For every digit:

Choose one letter.
Move to the next digit.
Continue until all digits are processed.

This forms a decision tree.


Visualization

Input:

digits = "23"

Phone mapping:

2 → abc

3 → def

Decision Tree:

                ""
          /      |      \
         a       b       c
      /  |  \  / | \   / | \
     d   e  f d e f  d e f


Possible combinations:

ad
ae
af
bd
be
bf
cd
ce
cf

Algorithm
If the input is empty, return [].
Create the phone mapping.
Use a recursive backtracking function.
For each letter of the current digit:
Add it to the current combination.
Recurse for the next digit.
Remove the letter (backtrack).
Store complete combinations.

  
Python Code
class Solution:
    def letterCombinations(self, digits):

        if not digits:
            return []

        phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        result = []

        def backtrack(index, path):

            if index == len(digits):
                result.append(path)
                return

            letters = phone[digits[index]]

            for letter in letters:
                backtrack(index + 1, path + letter)

        backtrack(0, "")

        return result
