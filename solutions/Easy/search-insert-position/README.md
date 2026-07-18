# Search Insert Position

**Difficulty:** Easy  
**LeetCode Link:** [Open Problem](https://leetcode.com/problems/search-insert-position/)

## Problem Description
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with `O(log n)` runtime complexity.

**Example 1:**

```
Input: nums = [1,3,5,6], target = 5
Output: 2
```

**Example 2:**

```
Input: nums = [1,3,5,6], target = 2
Output: 1
```

**Example 3:**

```
Input: nums = [1,3,5,6], target = 7
Output: 4
```

**Constraints:**

* `1 <= nums.length <= 104`
* `-104 <= nums[i] <= 104`
* `nums` contains **distinct** values sorted in **ascending** order.
* `-104 <= target <= 104`

## Solution

- **Language:** Python3
- **Time Complexity:** O(log N)
- **Space Complexity:** O(1)

### Approach
The problem requires finding the index of a target value in a sorted array, or the index where it should be inserted. This can be solved efficiently using binary search. We maintain two pointers, `left` and `right`. In each step, we check the middle element `mid`. If `nums[mid]` equals the target, we return `mid`. If `nums[mid]` is less than the target, we narrow our search to the right half by setting `left = mid + 1`. Otherwise, we search the left half by setting `right = mid - 1`. If the target is not found, the loop terminates when `left > right`, and `left` will point to the correct insertion index.

### Code
```py
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left
```
