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
