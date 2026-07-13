
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


Example 3
Input:
s = "ab"
p = ".*"

Output:
True

Explanation:

.

matches any character

*

matches any number of times

So .* matches everything.


Example 4
Input:
s = "mississippi"
p = "mis*is*p*."

Output:
False


Understanding the Operators
Dot (.)

Matches exactly one character.

Examples:

Pattern: a.c

Matches:

abc ✔

axc ✔

a9c ✔

Does not match:

ac
abbc
Star (*)

Matches zero or more of the previous character.

Example:

a*

Matches:

""

a

aa

aaa

aaaa
Dot + Star
.*

Means:

Any character

Any number of times

So it matches almost every string.


Why is this Hard?

At every *, there are multiple choices:

Example:

s = "aaa"

p = "a*"

Should * match:

0 a's?

1 a?

2 a's?

3 a's?

We must explore all valid possibilities efficiently.

This is why Dynamic Programming (DP) is used.

Approach 1: Recursion (Brute Force)
Idea

Compare characters from left to right.

At each *, choose one of two options:

Skip x*.
Use x* to match one more character.
Recursive Code


class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        def dfs(i, j):

            if j == len(p):
                return i == len(s)

            first_match = (
                i < len(s)
                and
                (s[i] == p[j] or p[j] == ".")
            )

            if j + 1 < len(p) and p[j + 1] == "*":

                return (
                    dfs(i, j + 2)
                    or
                    (first_match and dfs(i + 1, j))
                )

            return first_match and dfs(i + 1, j + 1)

        return dfs(0, 0)


Time Complexity
O(2^(m+n))

Very slow because many states are recalculated.

Approach 2: Dynamic Programming (Memoization)

Instead of solving the same subproblem repeatedly, store each result.

Idea

Use:

dp(i, j)

Meaning:

Does

s[i:]

match

p[j:] ?

If already solved, return the stored answer.

Python Code (Optimal)


class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        memo = {}

        def dp(i, j):

            if (i, j) in memo:
                return memo[(i, j)]

            if j == len(p):
                return i == len(s)

            first_match = (
                i < len(s)
                and
                (s[i] == p[j] or p[j] == ".")
            )

            if j + 1 < len(p) and p[j + 1] == "*":

                ans = (
                    dp(i, j + 2)
                    or
                    (first_match and dp(i + 1, j))
                )

            else:

                ans = first_match and dp(i + 1, j + 1)

            memo[(i, j)] = ans

            return ans


Line-by-Line Explanation
Memo Dictionary
memo = {}

Stores already computed states.

Key:

(i, j)

Example:

(3,2)

means:

String starts at index 3

Pattern starts at index 2
Base Case
if j == len(p):
    return i == len(s)

Pattern is finished.

String must also be finished.

Current Characters Match?
first_match = (
    i < len(s)
    and
    (s[i] == p[j] or p[j] == ".")
)

Example:

a == a ✔

b == . ✔

b == a ✖
Star Case
if j + 1 < len(p) and p[j + 1] == "*":

Pattern:

a*

We have two choices.

Option 1

Skip

dp(i, j + 2)

Ignore

a*
Option 2

Use one occurrence

first_match and dp(i + 1, j)

Consume one character.

Remain at the same pattern because * can match multiple times.

Normal Character
ans = first_match and dp(i + 1, j + 1)

Move both pointers forward.

Save Result
memo[(i, j)] = ans

Avoid recomputation.

Dry Run

Input:

s = "aa"

p = "a*"

Step 1

a matches a

Step 2

* found

Choices:

Skip *

OR

Consume one a

Consume:

a
↓

a

Consume again:

a

↓

empty

Pattern also finishes.

Answer:

True
        return dp(0, 0)
