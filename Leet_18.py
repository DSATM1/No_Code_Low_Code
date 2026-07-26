
LeetCode #18 – 4Sum

Difficulty: Medium

Problem Statement

Given an array nums of n integers, return all unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct indices.
nums[a] + nums[b] + nums[c] + nums[d] == target

The solution set must not contain duplicate quadruplets.

Example 1
Input:
nums = [1,0,-1,0,-2,2]
target = 0

Output:
[
[-2,-1,1,2],
[-2,0,0,2],
[-1,0,0,1]
]
Example 2
Input:
nums = [2,2,2,2,2]
target = 8

Output:
[
[2,2,2,2]
]


Approach 1: Brute Force
Idea

Check every possible group of four numbers.

If their sum equals the target, store the quadruplet.

Use a set to remove duplicates.

Python Code
class Solution:
    def fourSum(self, nums, target):

        nums.sort()
        n = len(nums)
        result = set()

        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    for l in range(k + 1, n):

                        if nums[i] + nums[j] + nums[k] + nums[l] == target:
                            result.add((nums[i], nums[j], nums[k], nums[l]))

        return [list(x) for x in result]
