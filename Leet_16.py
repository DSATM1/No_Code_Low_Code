
LeetCode #16 – 3Sum Closest

Difficulty: Medium

LeetCode #16 – 3Sum Closest

Difficulty: Medium

Problem Statement

Given an integer array nums of length n and an integer target, find three integers in nums such that their sum is closest to the target.

Return the sum of the three integers.

You may assume that each input has exactly one solution.
Example 1
Input:
nums = [-1,2,1,-4]
target = 1

Output:
2

Explanation:

Triplets:

(-1,2,1) = 2
(-4,2,1) = -1
(-4,-1,2) = -3
(-4,-1,1) = -4

Closest to target (1) is 2.
Example 2
Input:
nums = [0,0,0]
target = 1

Output:
0


Approach 1: Brute Force
Idea

Check every possible triplet.

Compute the difference between its sum and the target.

Keep the sum with the smallest difference.

Python Code
class Solution:
    def threeSumClosest(self, nums, target):

        n = len(nums)
        closest = nums[0] + nums[1] + nums[2]

        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):

                    total = nums[i] + nums[j] + nums[k]

                    if abs(total - target) < abs(closest - target):
                        closest = total

        return closest
Complexity
Time	Space
O(n³)	O(1)

Too slow for large inputs.

Approach 2: Sorting + Two Pointers (Optimal)

This is the expected interview solution.

Key Idea
Sort the array.
Fix one element.
Use two pointers to find the closest sum.

Unlike 3Sum (#15), we do not need to skip duplicate triplets, because we only return the closest sum.
