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


"""Optimal Approach – Sliding Window (Two Pointers)

This is the approach expected in interviews.

Idea

Maintain a window that always contains unique characters.

Use:

left → starting index
right → ending index
Dictionary to remember the last index of each character.

When a duplicate is found:

Move left to one position after the previous occurrence."""


"""Visualization

Suppose

s = "abcabcbb"

Start

Window = "a"
Length = 1

Expand

"ab"
Length = 2

Expand

"abc"
Length = 3

Next character is another 'a'

Current window

abc
^
duplicate

Move left after previous 'a'

Window becomes

bca

Continue until the end.

Maximum length remains 3."""

"""
Algorithm
Create an empty dictionary.
Initialize:
left = 0
max_len = 0
Traverse using right.
If character already exists inside current window:
Move left.
Update character's latest index.
Calculate current window size.
Update maximum."""


"""Python Code


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        char_index = {}

        left = 0
        max_len = 0

        for right in range(len(s)):

            if s[right] in char_index and char_index[s[right]] >= left:
                left = char_index[s[right]] + 1

            char_index[s[right]] = right

            current_length = right - left + 1

            max_len = max(max_len, current_length)

        return max_len"""



"""Line-by-Line Explanation
Dictionary
char_index = {}

Stores

character : last index

Example

{
'a':0,
'b':1,
'c':2
}
Left Pointer
left = 0

Beginning of current window.

Maximum Length
max_len = 0

Stores the final answer.

Loop
for right in range(len(s)):

Move the right pointer one character at a time.

Duplicate Check
if s[right] in char_index and char_index[s[right]] >= left:

Suppose

abcdea
     ^

The second 'a' is inside the current window.

Move left.

Move Left
left = char_index[s[right]] + 1

Example

a b c d a
0 1 2 3 4

Previous 'a' = index 0

New left

1

Window becomes

bcda
Update Latest Position
char_index[s[right]] = right

Always remember the latest occurrence.

Current Window Size
current_length = right - left + 1

Example

left = 2
right = 5

Length = 5 - 2 + 1 = 4
Update Answer
max_len = max(max_len, current_length)

Keep the largest window.

Return
return max_len"""

"""Dry Run

Input : s = "abcabcbb"

Right	Character	Left	Window	Max
0	    a	        0	    a	    1   
1	    b	        0	    ab	    2
2	    c	        0	    abc 	3
3	    a	        1	    bca 	3
4	    b	        2	    cab 	3
5	    c	        3	    abc 	3
6	    b	        5	    cb	    3
7	    b	        7	    b	    3   

Answer : 3"""


"""Complexity Analysis
Complexity	Value
Time	O(n)
Space	O(min(n, m)), where m is the size of the character set"""