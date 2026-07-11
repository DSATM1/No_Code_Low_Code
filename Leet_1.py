#This is only code description file
# LeetCode #1: Two Sum
The "Two Sum" problem is a classic algorithmic challenge. You are given an array of integers nums and an integer target. Your goal is to return the **indices** of the two numbers such that they add up to the target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
## 1. The Approaches
### Brute Force Approach
The simplest way to solve this is to use two nested loops to check every possible pair of numbers in the array.
 * **Time Complexity:** O(n^2) because for every element, you iterate through the rest of the array.
 * **Space Complexity:** O(1).
 * *Verdict:* Generally not accepted in interviews due to inefficiency.
### One-Pass Hash Map Approach (Optimal)
This approach reduces time complexity significantly by using a **Hash Map** (or Dictionary in Python) to store the numbers you have already visited.
As you iterate through the array, you calculate the complement (i.e., target - current_number). You check if that complement already exists in your hash map.
 * **Time Complexity:** O(n) because we only traverse the list once.
 * **Space Complexity:** O(n) because we store elements in the hash map.
## 2. Pseudocode (Optimal Approach)
```text
FUNCTION twoSum(nums, target):
    CREATE an empty Hash Map (named "seen")
    
    FOR index, value IN nums:
        COMPLEMENT = target - value
        
        IF COMPLEMENT exists in "seen":
            RETURN [seen[COMPLEMENT], index]
        
        ELSE:
            STORE value in "seen" with index as value (seen[value] = index)
            
    RETURN empty list (if no solution found)

```
## 3. Code Implementation (Python)
Here is the clean, efficient implementation of the One-Pass Hash Map strategy.
```python
def twoSum(nums, target):
    # Dictionary to store number: index
    seen = {}
    
    for i, num in enumerate(nums):
        complement = target - num
        
        # Check if the complement is already in our dictionary
        if complement in seen:
            return [seen[complement], i]
        
        # Otherwise, add the current number to the dictionary
        seen[num] = i
        
    return []

# Example usage:
# nums = [2, 7, 11, 15], target = 9
# Output: [0, 1]

```
### Why this works:
 1. **Speed:** Dictionary lookups in Python (Hash Maps) happen in O(1) constant time on average.
 2. **Memory-Speed Tradeoff:** We sacrifice a little bit of memory to store the seen dictionary in exchange for vastly improved processing speed.
