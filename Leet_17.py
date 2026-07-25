
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
