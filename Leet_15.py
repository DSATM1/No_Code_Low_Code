
LeetCode #15 – 3Sum

Difficulty: Medium

Problem Statement

Given an integer array nums, return all unique triplets [nums[i], nums[j], nums[k]] such that:

i != j
i != k
j != k
nums[i] + nums[j] + nums[k] == 0

The solution set must not contain duplicate triplets.
Example 1
Input:
nums = [-1,0,1,2,-1,-4]

Output:
[[-1,-1,2],[-1,0,1]]
Example 2
Input:
nums = [0,1,1]

Output:
[]
Example 3
Input:
nums = [0,0,0]

Output:
[[0,0,0]]
Approach 1: Brute Force
Idea

Check every possible triplet.

If the sum is 0, add it to the answer.

Use a set to avoid duplicates.

Python Code
class Solution:
    def threeSum(self, nums):

        ans = set()

        n = len(nums)

        for i in range(n):

            for j in range(i + 1, n):

                for k in range(j + 1, n):

                    if nums[i] + nums[j] + nums[k] == 0:

                        triplet = tuple(sorted([nums[i], nums[j], nums[k]]))
                        ans.add(triplet)

        return [list(x) for x in ans]
Complexity
Time	Space
O(n³)	O(n)

Too slow for large inputs.

Approach 2: Sorting + Two Pointers (Optimal)

This is the standard interview solution.

Key Idea
Sort the array.
Fix one element.
Use two pointers to find the remaining two numbers whose sum equals -nums[i].
Why Sort?

Sorting helps:

Use two pointers efficiently.
Skip duplicate values easily.
Visualization

Input:

[-1,0,1,2,-1,-4]

After sorting:

[-4,-1,-1,0,1,2]

Fix:

i = -1

Need:

left + right = 1

Move pointers until the sum is found.

Algorithm
Sort the array.
Traverse each element as the first number.
Skip duplicate first elements.
Set:
left = i + 1
right = n - 1
Calculate:
total = nums[i] + nums[left] + nums[right]
If:
total == 0 → Save triplet.
total < 0 → Move left.
total > 0 → Move right.
Skip duplicate values for left and right.
Python Code
class Solution:
    def threeSum(self, nums):

        nums.sort()

        result = []

        n = len(nums)

        for i in range(n - 2):

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = n - 1

            while left < right:

                total = nums[i] + nums[left] + nums[right]

                if total == 0:

                    result.append([nums[i], nums[left], nums[right]])

                    while left < right and nums[left] == nums[left + 1]:
                        left += 1

                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

                elif total < 0:
                    left += 1

                else:
                    right -= 1

        return result
