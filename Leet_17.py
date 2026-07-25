
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


Line-by-Line Explanation
Step 1: Empty Input
if not digits:
    return []

Example:

digits = ""

Answer = []
Step 2: Phone Mapping
phone = {
    "2":"abc",
    "3":"def",
    ...
}

This dictionary tells us which letters belong to each digit.

Step 3: Result List
result = []

Stores all valid combinations.

Step 4: Backtracking Function
def backtrack(index, path):

Parameters:

index → Current digit being processed.
path → Current letter combination.
Step 5: Base Case
if index == len(digits):
    result.append(path)
    return

If all digits are processed, store the completed combination.

Step 6: Get Letters
letters = phone[digits[index]]

Example:

digits[index] = "2"

letters = "abc"
Step 7: Try Every Letter
for letter in letters:

For "abc":

a
b
c
Step 8: Recursive Call
backtrack(index + 1, path + letter)

Example:

path = ""

↓

a

↓

ad

↓

Store "ad"


Dry Run

Input:

digits = "23"

Tree:

           ""
        /   |   \
       a    b    c
     / | \ /|\  /|\
    d e f d e f d e f

Generated combinations:

Combination
ad
ae
af
bd
be
bf
cd
ce
cf

Output:

[
"ad","ae","af",
"bd","be","bf",
"cd","ce","cf"
]


Complexity Analysis

Let:

n = number of digits.
Each digit has up to 4 letters (7 and 9).
Complexity	Value
Time	      O(4ⁿ × n)
Space	      O(n) (excluding the output list)

The × n factor comes from building strings of length n.


Pattern Used

This problem is a classic Backtracking problem.

Recognition Clues
Generate all possible combinations.
Make one choice at a time.
Undo the choice and explore the next option.
Explore a decision tree recursively.
Similar Problems
LeetCode #22 – Generate Parentheses
LeetCode #39 – Combination Sum
LeetCode #46 – Permutations
LeetCode #77 – Combinations
LeetCode #78 – Subsets
