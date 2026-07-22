
LeetCode #14 – Longest Common Prefix

Difficulty: Easy
Problem Statement

Write a function to find the longest common prefix string among an array of strings.

If there is no common prefix, return an empty string "".
Example 1
Input:
strs = ["flower","flow","flight"]

Output:
"fl"

Explanation:

flower
flow
flight

Common prefix:

fl

Example 2
Input:
strs = ["dog","racecar","car"]

Output:
""

Explanation:

There is no common prefix.

Approach 1: Horizontal Scanning (Interview Preferred)
Idea
Assume the first string is the common prefix.
Compare it with every other string.
Shorten the prefix until it matches.
