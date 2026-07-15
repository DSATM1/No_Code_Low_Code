
LeetCode #11 – Container With Most Water

Difficulty: Medium
Problem Statement

You are given an integer array height, where each element represents the height of a vertical line.

Choose two lines such that together with the x-axis they form a container that holds the maximum amount of water.

Return the maximum amount of water.
Example 1
Input:
height = [1,8,6,2,5,4,8,3,7]

Output:
49

Visualization:

Height

8 |      |                     |
7 |      |                   __|
6 |      |     |            |  |
5 |      |     |    |       |  |
4 |      |     |    |   |   |  |
3 |      |     |    |   |   |  |
2 |      |  |  |    |   |   |  |
1 | |    |  |  | |  | | | | |  |
  +-------------------------------
    0 1 2 3 4 5 6 7 8

Best container:

Left = height[1] = 8
Right = height[8] = 7
Width = 8 - 1 = 7
Height = min(8, 7) = 7

Area:

7 × 7 = 49


Example 2
Input:
height = [1,1]

Output:
1


Formula

The water stored between two lines is:

Area = Width × Height

Where:

Width = right - left

Height = min(height[left], height[right])

Therefore,

Area = (right - left) × min(height[left], height[right])


Approach 1: Brute Force
Idea

Check every possible pair of lines and calculate the area.

Keep track of the maximum area.

Python Code

class Solution:
    def maxArea(self, height):

        maximum = 0

        for i in range(len(height)):
            for j in range(i + 1, len(height)):

                area = (j - i) * min(height[i], height[j])

                maximum = max(maximum, area)

        return maximum


Complexity

Time:

O(n²)

Space:

O(1)

This solution gets accepted for small inputs but is inefficient for large arrays.


Approach 2: Two Pointers (Optimal)

This is the expected interview solution.

Key Idea

Start with the widest possible container:

Left pointer at the beginning.
Right pointer at the end.

Calculate the area.

Then move the pointer with the smaller height, because moving the taller line cannot increase the area—the shorter line limits the water height.

Why Move the Smaller Height?

Suppose:

Left Height = 3
Right Height = 8

Current area:

Width × 3

If we move the taller line (height 8):

Width decreases.
Limiting height is still 3 (or lower).

So the area cannot improve.

To potentially increase the limiting height, move the shorter line.                                                               


Algorithm
Place one pointer at the beginning.
Place another pointer at the end.
Calculate the current area.
Update the maximum area.
Move the pointer with the smaller height.
Repeat until the pointers meet.


class Solution:
    def maxArea(self, height):

        left = 0
        right = len(height) - 1

        maximum = 0

        while left < right:

            width = right - left

            current_height = min(height[left], height[right])

            area = width * current_height

            maximum = max(maximum, area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return maximum

Line-by-Line Explanation
Step 1: Initialize Pointers
left = 0
right = len(height) - 1

Start from both ends of the array.

Step 2: Store Maximum Area
maximum = 0

This variable keeps track of the best answer found so far.

Step 3: Continue Until Pointers Meet
while left < right:

Each iteration considers one possible container.

Step 4: Calculate Width
width = right - left

Example:

left = 1
right = 8

Width = 7
Step 5: Find Effective Height
current_height = min(height[left], height[right])

The shorter line determines how much water can be stored.

Step 6: Calculate Area
area = width * current_height

Example:

Width = 7

Height = 7

Area = 49
Step 7: Update Maximum
maximum = max(maximum, area)

Keep the largest area found.

Step 8: Move the Shorter Line
if height[left] < height[right]:
    left += 1
else:
    right -= 1

This gives the only chance to increase the container's height while the width decreases.
Dry Run

Input:

height = [1,8,6,2,5,4,8,3,7]
Left	Right	Width	Min Height	Area	Max
0	Dry Run
Input:

height = [1,8,6,2,5,4,8,3,7]
Left	Right	Width	MinHeight	Area	Max
0	    8	    8	    1	        8	    8
1	    8	    7	    7	        49	  49
1	    7	    6	    3	        18	  49
1	    6	    5	    8	        40	  49
2	    6	    4	    6	        24	  49
3	    6	    3	    2	        6	    49
4	    6	    2	    5	        10	  49
5	    6	    1	    4	        4	    49

Final answer: 49

Complexity Analysis
Approach	    Time	  Space
Brute Force	  O(n²)	  O(1)
Two Pointers	O(n)	  O(1)


Pattern Used

This problem is a classic Two Pointers problem.

Recognition Clues
Array input.
Need to compare values from both ends.
Want an optimal solution better than O(n²).
Decision at each step is based on comparing two values.
Similar Two-Pointer Problems
LeetCode #15 – 3Sum
LeetCode #42 – Trapping Rain Water
LeetCode #125 – Valid Palindrome
LeetCode #167 – Two Sum II (Sorted Array)
LeetCode #344 – Reverse String

This is one of the most frequently asked Two Pointer interview problems, 
so it's worth understanding the reasoning behind why the shorter 
pointer is moved rather than memorizing the code.
