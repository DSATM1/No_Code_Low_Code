LeetCode #4 – Median of Two Sorted Arrays

Difficulty: Hard


---

Problem Statement

Given two sorted arrays nums1 and nums2 of sizes m and n, return the median of the two sorted arrays.

The overall runtime complexity should be O(log(m + n)).


---

Example 1

Input:
nums1 = [1, 3]
nums2 = [2]

Output:
2.0

Explanation:
Merged array = [1, 2, 3]
Median = 2


---

Example 2

Input:
nums1 = [1, 2]
nums2 = [3, 4]

Output:
2.5

Explanation:
Merged array = [1, 2, 3, 4]
Median = (2 + 3) / 2 = 2.5


---

What is Median?

If the number of elements is odd, the median is the middle element.

Example:

[1, 2, 3]

Median = 2

If the number of elements is even, the median is the average of the two middle elements.

Example:

[1, 2, 3, 4]

Median = (2 + 3) / 2 = 2.5


---

Approach 1: Brute Force (Merge Arrays)

Idea

1. Merge both sorted arrays.


2. Find the middle element(s).


3. Return the median.



Algorithm

1. Combine the arrays.


2. Sort the combined array.


3. Find the median based on the total number of elements.




---

Python Code

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):

        nums = sorted(nums1 + nums2)

        n = len(nums)

        if n % 2 == 1:
            return nums[n // 2]

        return (nums[n // 2] + nums[n // 2 - 1]) / 2


---

Time Complexity

Merge = O(m + n)

Sort = O((m + n) log(m + n))


Overall:

O((m+n) log(m+n))

Space:

O(m+n)

This works but does not satisfy the required complexity.


---

Approach 2: Merge Using Two Pointers (Better, but Still Not Optimal)

Instead of sorting again, take advantage of the fact that both arrays are already sorted.

Idea

Use two pointers to merge them into a new sorted array.

Python Code

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):

        i = 0
        j = 0
        merged = []

        while i < len(nums1) and j < len(nums2):

            if nums1[i] <= nums2[j]:
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                j += 1

        while i < len(nums1):
            merged.append(nums1[i])
            i += 1

        while j < len(nums2):
            merged.append(nums2[j])
            j += 1

        n = len(merged)

        if n % 2:
            return merged[n // 2]

        return (merged[n // 2] + merged[n // 2 - 1]) / 2

Complexity

Time:

O(m+n)

Space:

O(m+n)

Still not accepted for the intended interview solution because the problem asks for O(log(m+n)).


---

Approach 3: Binary Search (Optimal)

This is the expected interview solution.

Main Idea

Instead of merging the arrays, partition them into left and right halves.

The partition is correct when:

max(left1, left2) <= min(right1, right2)

Then:

If the total number of elements is odd, the median is the maximum element on the left side.

If the total number of elements is even, the median is the average of the maximum left element and the minimum right element.



---

Example

nums1 = [1,3]
nums2 = [2]

Partitions:

nums1 : 1 | 3
nums2 :   | 2

Left side:

1 2

Right side:

3

Median:

2


---

Binary Search Algorithm

1. Perform binary search on the smaller array.


2. Choose a partition in the first array.


3. Compute the corresponding partition in the second array.


4. Check whether the partition is valid.


5. If not:

Move left if left1 > right2

Move right otherwise.



6. Return the median when the partition is valid.




---

Optimal Python Code

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):

        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m = len(nums1)
        n = len(nums2)

        left = 0
        right = m

        while left <= right:

            partition1 = (left + right) // 2
            partition2 = (m + n + 1) // 2 - partition1

            maxLeft1 = float('-inf') if partition1 == 0 else nums1[partition1 - 1]
            minRight1 = float('inf') if partition1 == m else nums1[partition1]

            maxLeft2 = float('-inf') if partition2 == 0 else nums2[partition2 - 1]
            minRight2 = float('inf') if partition2 == n else nums2[partition2]

            if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:

                if (m + n) % 2 == 0:
                    return (max(maxLeft1, maxLeft2) +
                            min(minRight1, minRight2)) / 2

                return max(maxLeft1, maxLeft2)

            elif maxLeft1 > minRight2:
                right = partition1 - 1

            else:
                left = partition1 + 1


---

Dry Run

Input:

nums1 = [1,2]
nums2 = [3,4]

Total elements:

4

Correct partition:

Left:
1 2

Right:
3 4

Median:

(2 + 3)/2 = 2.5


---

Complexity Analysis

Approach	Time	Space

Merge + Sort	O((m+n) log(m+n))	O(m+n)
Two-Pointer Merge	O(m+n)	O(m+n)
Binary Search (Optimal)	O(log(min(m,n)))	O(1)



---

Pattern Used

The optimal solution combines:

Binary Search

Partitioning

Sorted Arrays

Divide and Conquer


This is considered one of the most challenging binary search problems on LeetCode because the binary search is performed on the partition position, not on the array values themselves.
