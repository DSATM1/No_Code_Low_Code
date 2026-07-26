
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


Complexity
Time	Space
O(n⁴)	O(n)

Too slow for large inputs.

Approach 2: Sorting + Two Pointers (Optimal)

This is the expected interview solution.

Key Idea

This is an extension of 3Sum.

Sort the array.
Fix the first number (i).
Fix the second number (j).
Use two pointers (left, right) to find the remaining two numbers.

Visualization

Input:

nums = [1,0,-1,0,-2,2]
target = 0

After sorting:

[-2,-1,0,0,1,2]

Fix:

i = -2
j = -1

Need:

left + right = 3

Use two pointers to search.

Algorithm
Sort the array.
Loop through the first element (i).
Skip duplicate values for i.
Loop through the second element (j).
Skip duplicate values for j.
Set:
left = j + 1
right = n - 1
Calculate the sum.
If:
Sum == target → Save quadruplet.
Sum < target → Move left.
Sum > target → Move right.
Skip duplicate values for left and right.

Python Code
class Solution:
    def fourSum(self, nums, target):

        nums.sort()
        result = []
        n = len(nums)

        for i in range(n - 3):

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, n - 2):

                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                left = j + 1
                right = n - 1

                while left < right:

                    total = nums[i] + nums[j] + nums[left] + nums[right]

                    if total == target:

                        result.append([
                            nums[i],
                            nums[j],
                            nums[left],
                            nums[right]
                        ])

                        while left < right and nums[left] == nums[left + 1]:
                            left += 1

                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1

                        left += 1
                        right -= 1

                    elif total < target:
                        left += 1

                    else:
                        right -= 1

        return result
