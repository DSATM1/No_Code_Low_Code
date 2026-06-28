"""LeetCode #3 – Longest Substring Without Repeating Characters

Difficulty: Medium

Problem Statement

Given a string s, find the length of the longest substring without repeating characters.

A substring means the characters must be continuous."""

"""Example 1

Input: s = "abcabcbb"

Output: 3

Explanation:
The longest substring is "abc", so the answer is 3."""

"""Example 2
Input: s = "bbbbb"

Output: 1

Explanation:
The longest substring is "b"."""

"""Example 3
Input: s = "pwwkew"

Output: 3

Explanation:
The longest substring is "wke"."""

"""Brute Force Approach
Idea
Generate every possible substring.
Check if all characters are unique.
Keep track of the maximum length.
Time Complexity
O(n³)
O(n²) to generate substrings
O(n) to check duplicates

Not efficient for large inputs."""