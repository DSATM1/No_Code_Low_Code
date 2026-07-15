
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


