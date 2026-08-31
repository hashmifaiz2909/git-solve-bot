# Search in Rotated Sorted Array

**Difficulty:** Medium  
**LeetCode Link:** [Open Problem](https://leetcode.com/problems/search-in-rotated-sorted-array/)

## Problem Description
There is an integer array `nums` sorted in ascending order (with **distinct** values).

Prior to being passed to your function, `nums` is **possibly left rotated** at an unknown index `k` (`1 <= k < nums.length`) such that the resulting array is `[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]` (**0-indexed**). For example, `[0,1,2,4,5,6,7]` might be left rotated by `3` indices and become `[4,5,6,7,0,1,2]`.

Given the array `nums` **after** the possible rotation and an integer `target`, return *the index of* `target` *if it is in* `nums`*, or* `-1` *if it is not in* `nums`.

You must write an algorithm with `O(log n)` runtime complexity.

**Example 1:**

```
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
```

**Example 2:**

```
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
```

**Example 3:**

```
Input: nums = [1], target = 0
Output: -1
```

**Constraints:**

* `1 <= nums.length <= 5000`
* `-104 <= nums[i] <= 104`
* All values of `nums` are **unique**.
* `nums` is an ascending array that is possibly rotated.
* `-104 <= target <= 104`

## Solution

- **Language:** Python3
- **Time Complexity:** O(log N)
- **Space Complexity:** O(1)

### Approach
The algorithm uses a modified binary search. In any rotated sorted array, at least one of the two halves (left or right) is always sorted. By comparing the middle element with the leftmost element, we can determine which half is sorted. If the left half is sorted, we check if the target lies within its range; if so, we narrow our search to the left half, otherwise we search the right half. If the right half is sorted, we perform a similar check for the target in the right half's range. This allows us to discard half of the search space in each step, achieving logarithmic time complexity.

### Code
```py
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            
            # Check if the left half is sorted
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            # Otherwise, the right half must be sorted
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
                    
        return -1
```
