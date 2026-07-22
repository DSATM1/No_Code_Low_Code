
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

Algorithm
Set the first string as the prefix.
Compare it with each remaining string.
While the current string doesn't start with the prefix:
Remove the last character from the prefix.
If the prefix becomes empty, return "".
Return the final prefix.

Python Code
class Solution:
    def longestCommonPrefix(self, strs):
        
        if not strs:
            return ""

        prefix = strs[0]

        for s in strs[1:]:

            while not s.startswith(prefix):
                prefix = prefix[:-1]

                if prefix == "":
                    return ""

        return prefix


Line-by-Line Explanation
Step 1: Handle Empty List
if not strs:
    return ""

If the input list is empty, there is no common prefix.


Step 2: Assume First String as Prefix
prefix = strs[0]

Example:

["flower","flow","flight"]

prefix = "flower"

Step 3: Compare with Remaining Strings
for s in strs[1:]:

Compare "flower" with:

"flow"
"flight"

Step 4: Shorten Prefix
while not s.startswith(prefix):

If the current string doesn't start with the prefix, remove the last character.

Example:

prefix = "flower"

flow

Shorten:

flower
flowe
flow

Now "flow".startswith("flow") is True.
