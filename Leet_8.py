LeetCode 8: String to Integer (atoi)
The Problem Requirements
The goal is to convert a string into a 32-bit signed integer. 
The algorithm must follow these strict rules:
Whitespace: 
Ignore any leading whitespace (" ").
Sign: 
Check if the next character is '-' or '+'.
Assume it is positive if neither is present.
Conversion: Read the characters until the next non-digit character or the end of the string. 
Convert these digits into an integer.
Clamping: If the integer is out of the 32-bit signed integer range $[-2^{31}, 2^{31} - 1]$, 
clamp it so it remains within the range.

Approach
The best way to solve this is through a sequential string parsing approach 
(often called a Deterministic Finite Automaton or simple pointer iteration).

Strip Whitespace: Remove leading spaces to clean up the start of the string. 
If the string becomes empty, return 0.

Determine the Sign: Check the first character of the cleaned string.
If it's a -, record the sign as -1 and advance the index. If it's +, just advance the index.

Build the Integer: Iterate through the remaining string character by character.

If the character is a digit, multiply the current result by 10 and add the integer value of the character.

If the character is not a digit, immediately break the loop (ignore the rest of the string).

Apply Sign and Clamp: Multiply the final result by the sign. Finally, 
check if the result exceeds the 32-bit bounds and clamp it if necessary.


class Solution:
    def myAtoi(self, s: str) -> int:
        # 1. Remove leading whitespace
        s = s.lstrip()
        
        # If string is empty after stripping, return 0
        if not s:
            return 0
        
        # 2. Initialize variables
        sign = 1
        index = 0
        result = 0
        
        # 3. Handle sign
        if s[index] == '-':
            sign = -1
            index += 1
        elif s[index] == '+':
            index += 1
            
        # 4. Process numerical characters
        while index < len(s) and s[index].isdigit():
            # Convert string char to int and add to result
            result = result * 10 + int(s[index])
            index += 1
            
        # Apply the sign
        result *= sign
        
        # 5. Clamp to 32-bit signed integer range
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1
        
        if result < INT_MIN:
            return INT_MIN
        elif result > INT_MAX:
            return INT_MAX
            
        return result



Complexity Analysis

Time Complexity: 
$\mathcal{O}(N)$ where $N$ is the length of the string. 
We iterate through the characters of the string at most once.


Space Complexity: $\mathcal{O}(1)$. 
We are only using a few variables (sign, index, result, and bounds) which require constant extra space.

Common Edge Cases Handled:

"   -42": Successfully strips spaces and catches the negative sign.
"4193 with words": Stops reading at the first space/letter and correctly returns 4193.
"words and 987": The first non-space character is a letter (w), so the loop never processes digits. 
Returns 0.
    "-91283472332": Number gets processed but hits the clamping threshold, returning $-2^{31}$ ($-2147483648$).
