
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

Algorithm
Sort the array.
Initialize the closest sum using the first three elements.
Traverse the array.
Fix one element.
Use two pointers:
left = i + 1
right = n - 1
Calculate the current sum.
Update the closest sum if needed.
If:
Sum < target → move left.
Sum > target → move right.
Sum == target → return immediately.

Python Code
class Solution:
    def threeSumClosest(self, nums, target):

        nums.sort()

        closest = nums[0] + nums[1] + nums[2]

        n = len(nums)

        for i in range(n - 2):

            left = i + 1
            right = n - 1

            while left < right:

                total = nums[i] + nums[left] + nums[right]

                if abs(total - target) < abs(closest - target):
                    closest = total

                if total < target:
                    left += 1

                elif total > target:
                    right -= 1

                else:
                    return total

        return closest


Line-by-Line Explanation
Step 1: Sort the Array
nums.sort()

Example:

[-1,2,1,-4]

↓

[-4,-1,1,2]
Step 2: Initialize Closest
closest = nums[0] + nums[1] + nums[2]

This gives an initial candidate.

Step 3: Traverse
for i in range(n - 2):

Fix one element.

Step 4: Two Pointers
left = i + 1
right = n - 1
Step 5: Calculate Sum
total = nums[i] + nums[left] + nums[right]
Step 6: Update Closest
if abs(total - target) < abs(closest - target):
    closest = total

Choose the sum with the smallest absolute difference.

Step 7: Move Pointers
if total < target:
    left += 1

Need a larger sum.

elif total > target:
    right -= 1

Need a smaller sum.

else:
    return total

Exact match found.

Dry Run
Input
nums = [-1,2,1,-4]
target = 1

Sorted:

[-4,-1,1,2]

Initial:

closest = -4
i	Left	Right	Sum	    Closest
-4	-1	    2	    -3	    -3
-4	1	    2	    -1	    -1
-1	1	    2	    2	    2

Output:

2

Complexity Analysis
Approach	            Time	Space
Brute Force	            O(n³)	O(1)
Sorting + Two Pointers	O(n²)	O(1)
