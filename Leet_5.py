# LeetCode #5 – Longest Palindromic Substring

**Difficulty:** Medium

---

# Problem Statement

Given a string `s`, return the **longest palindromic substring** in `s`.

A **palindrome** is a string that reads the same forwards and backwards.

A **substring** is a contiguous sequence of characters.

---

## Example 1

```text
Input:
s = "babad"

Output:
"bab"

Explanation:
"aba" is also a valid answer.
```

---

## Example 2

```text
Input:
s = "cbbd"

Output:
"bb"
```

---

## Example 3

```text
Input:
s = "a"

Output:
"a"
```

---

## Example 4

```text
Input:
s = "ac"

Output:
"a"
```

---

# Approach 1: Brute Force

## Idea

1. Generate every possible substring.
2. Check if the substring is a palindrome.
3. Store the longest palindrome found.

---

## Algorithm

1. Generate all substrings using two loops.
2. Reverse each substring and compare it with the original.
3. Keep the longest palindrome.

---

## Python Code

```python
class Solution:
    def longestPalindrome(self, s: str) -> str:

        longest = ""

        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):

                substring = s[i:j]

                if substring == substring[::-1]:

                    if len(substring) > len(longest):
                        longest = substring

        return longest
```

---

## Time Complexity

There are O(n²) substrings, and checking each palindrome takes O(n).

```text
Time = O(n³)
Space = O(1)
```

---

# Approach 2: Expand Around Center (Optimal)

This is the most common interview solution.

## Key Idea

Every palindrome has a center.

There are two cases:

### 1. Odd-Length Palindrome

Example:

```text
racecar

    e
```

Expand outward from the center.

---

### 2. Even-Length Palindrome

Example:

```text
abba

  ||
```

The center is between two characters.

---

## Visualization

Input:

```text
babad
```

Choose center at `'a'`

```text
b a b
```

Expand:

```text
left  = b
right = b
```

Palindrome:

```text
bab
```

---

Choose center at second `'b'`

```text
a b a
```

Palindrome:

```text
aba
```

Longest length = 3.

---

# Algorithm

For every index:

1. Expand for odd palindrome.
2. Expand for even palindrome.
3. Store the longest palindrome.

---

# Python Code

```python
class Solution:
    def longestPalindrome(self, s: str) -> str:

        if len(s) <= 1:
            return s

        start = 0
        end = 0

        def expand(left, right):

            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            return left + 1, right - 1

        for i in range(len(s)):

            left1, right1 = expand(i, i)
            left2, right2 = expand(i, i + 1)

            if right1 - left1 > end - start:
                start, end = left1, right1

            if right2 - left2 > end - start:
                start, end = left2, right2

        return s[start:end + 1]
```

---

# Line-by-Line Explanation

### Step 1: Handle Small Strings

```python
if len(s) <= 1:
    return s
```

If the string has one or zero characters, it is already a palindrome.

---

### Step 2: Initialize Result

```python
start = 0
end = 0
```

These variables store the start and end indices of the longest palindrome found.

---

### Step 3: Expand Function

```python
def expand(left, right):
```

Expands outward while the characters on both sides are equal.

Example:

```
racecar
   ^
```

or

```
abba
 ||
```

---

### Step 4: Expand While Valid

```python
while left >= 0 and right < len(s) and s[left] == s[right]:
```

Continue expanding until:

* `left` goes out of bounds.
* `right` goes out of bounds.
* Characters no longer match.

---

### Step 5: Return Palindrome Boundaries

```python
return left + 1, right - 1
```

After the loop stops, `left` and `right` have moved one step too far, so adjust them back.

---

### Step 6: Check Both Palindrome Types

```python
left1, right1 = expand(i, i)
left2, right2 = expand(i, i + 1)
```

* `expand(i, i)` handles odd-length palindromes.
* `expand(i, i + 1)` handles even-length palindromes.

---

### Step 7: Update Longest Palindrome

```python
if right1 - left1 > end - start:
    start, end = left1, right1
```

Repeat the same check for the even-length palindrome.

---

### Step 8: Return Result

```python
return s[start:end + 1]
```

Return the longest palindromic substring.

---

# Dry Run

Input:

```text
s = "babad"
```

| Center | Palindrome | Longest      |
| ------ | ---------- | ------------ |
| b      | b          | b            |
| a      | bab        | bab          |
| b      | aba        | bab (or aba) |
| a      | a          | bab          |
| d      | d          | bab          |

Answer:

```text
"bab"
```

(LeetCode also accepts `"aba"`.)

---

# Complexity Analysis

| Approach             | Time      | Space    |
| -------------------- | --------- | -------- |
| Brute Force          | O(n³)     | O(1)     |
| Expand Around Center | **O(n²)** | **O(1)** |

---

# Advanced Approach (Not Required for Most Interviews)

There is an even faster algorithm called **Manacher's Algorithm**.

* **Time Complexity:** O(n)
* **Space Complexity:** O(n)

However, it is considerably more complex and is rarely expected in coding interviews. The **Expand Around Center** approach is the standard solution accepted in interviews and performs well for typical constraints.

---

# Pattern Used

This problem is a classic example of the **Expand Around Center** technique, which is useful for finding palindromic substrings efficiently. It is a common interview pattern alongside sliding window, two pointers, and binary search.

