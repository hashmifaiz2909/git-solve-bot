# Find First and Last Position of Element in Sorted Array

**Difficulty:** Medium  
**LeetCode Link:** [Open Problem](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/)

## Problem Description
Given an array of integers `nums` sorted in non-decreasing order, find the starting and ending position of a given `target` value.

If `target` is not found in the array, return `[-1, -1]`.

You must write an algorithm with `O(log n)` runtime complexity.

**Example 1:**

```
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
```

**Example 2:**

```
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
```

**Example 3:**

```
Input: nums = [], target = 0
Output: [-1,-1]
```

**Constraints:**

* `0 <= nums.length <= 105`
* `-109 <= nums[i] <= 109`
* `nums` is a non-decreasing array.
* `-109 <= target <= 109`

## Solution

- **Language:** Python3
- **Time Complexity:** O(log N)
- **Space Complexity:** O(1)

### Approach
The problem requires finding the starting and ending positions of a target value in a sorted array in O(log n) time. We can achieve this by performing two binary searches. The helper function `findBound(isFirst)` performs a binary search. If `isFirst` is True, it searches for the first occurrence of the target by continuing to search the left half even after finding a match. If `isFirst` is False, it searches for the last occurrence by continuing to search the right half. If the first occurrence is not found (returns -1), we can immediately return [-1, -1] without performing the second search.

### Code
```py
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findBound(isFirst: bool) -> int:
            left, right = 0, len(nums) - 1
            bound = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    bound = mid
                    if isFirst:
                        right = mid - 1
                    else:
                        left = mid + 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return bound
        
        first = findBound(True)
        if first == -1:
            return [-1, -1]
        return [first, findBound(False)]
```
