
LeetCode #10 – Regular Expression Matching

Difficulty: Hard
Problem Statement

Given an input string s and a pattern p, implement regular expression matching with support for:

. → Matches any single character.
* → Matches zero or more of the preceding element.

The match must cover the entire string, not just part of it.
Examples
Example 1
Input:
s = "aa"
p = "a"

Output:
False

Explanation:

Pattern: a
String : aa

Only one 'a' is matched.


Example 2
Input:
s = "aa"
p = "a*"

Output:
True

Explanation:

a* means:

0 or more 'a'

aa ✔
