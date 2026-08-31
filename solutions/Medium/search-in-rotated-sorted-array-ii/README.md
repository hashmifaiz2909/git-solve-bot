# Search in Rotated Sorted Array II

**Difficulty:** Medium  
**LeetCode Link:** [Open Problem](https://leetcode.com/problems/search-in-rotated-sorted-array-ii/)

## Problem Description
There is an integer array `nums` sorted in non-decreasing order (not necessarily with **distinct** values).

Before being passed to your function, `nums` is **rotated** at an unknown pivot index `k` (`0 <= k < nums.length`) such that the resulting array is `[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]` (**0-indexed**). For example, `[0,1,2,4,4,4,5,6,6,7]` might be rotated at pivot index `5` and become `[4,5,6,6,7,0,1,2,4,4]`.

Given the array `nums` **after** the rotation and an integer `target`, return `true` *if* `target` *is in* `nums`*, or* `false` *if it is not in* `nums`*.*

You must decrease the overall operation steps as much as possible.

**Example 1:**

```
Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true
```

**Example 2:**

```
Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false
```

**Constraints:**

* `1 <= nums.length <= 5000`
* `-104 <= nums[i] <= 104`
* `nums` is guaranteed to be rotated at some pivot.
* `-104 <= target <= 104`

**Follow up:** This problem is similar to [Search in Rotated Sorted Array](/problems/search-in-rotated-sorted-array/description/), but `nums` may contain **duplicates**. Would this affect the runtime complexity? How and why?

## Solution

- **Language:** Python3
- **Time Complexity:** O(N) in the worst case (when all elements are duplicates, e.g., [1, 1, 1, 1] and target is 0), but O(log N) on average.
- **Space Complexity:** O(1) auxiliary space as we only use a few pointers.

### Approach
The algorithm uses a modified binary search. In a rotated sorted array, at least one half of the array (left or right of the middle element) is always sorted. We can determine which half is sorted and check if the target lies within its boundaries. However, because the array can contain duplicates, we might encounter a case where nums[left] == nums[mid] == nums[right]. In this scenario, we cannot determine which half is sorted, so we shrink the search space by incrementing left and decrementing right. Otherwise, we proceed with standard binary search logic on the sorted half.

### Code
```py
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return True
            
            # If we cannot determine which half is sorted due to duplicates
            if nums[left] == nums[mid] == nums[right]:
                left += 1
                right -= 1
            # If the left half is sorted
            elif nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            # If the right half is sorted
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
                    
        return False
```
