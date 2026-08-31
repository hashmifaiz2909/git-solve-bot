# 4Sum

**Difficulty:** Medium  
**LeetCode Link:** [Open Problem](https://leetcode.com/problems/4sum/)

## Problem Description
Given an array `nums` of `n` integers, return *an array of all the **unique** quadruplets* `[nums[a], nums[b], nums[c], nums[d]]` such that:

* `0 <= a, b, c, d < n`
* `a`, `b`, `c`, and `d` are **distinct**.
* `nums[a] + nums[b] + nums[c] + nums[d] == target`

You may return the answer in **any order**.

**Example 1:**

```
Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
```

**Example 2:**

```
Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]
```

**Constraints:**

* `1 <= nums.length <= 200`
* `-109 <= nums[i] <= 109`
* `-109 <= target <= 109`

## Solution

- **Language:** Python3
- **Time Complexity:** O(N^3)
- **Space Complexity:** O(1)

### Approach
The algorithm sorts the input array first to easily handle duplicates and use the two-pointer technique. It uses two nested loops to fix the first two elements, and then a two-pointer approach to find the remaining two elements. To optimize performance, several pruning steps are added: we break early if the minimum possible sum exceeds the target, and we skip the current iteration if the maximum possible sum is less than the target. Duplicate quadruplets are avoided by skipping identical adjacent elements during the loops and pointer movements.

### Code
```py
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        results = []
        
        for i in range(n - 3):
            # Avoid duplicates for the first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # Optimization: if the smallest possible sum is greater than target, break
            if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:
                break
            # Optimization: if the largest possible sum with nums[i] is less than target, skip
            if nums[i] + nums[n - 3] + nums[n - 2] + nums[n - 1] < target:
                continue
                
            for j in range(i + 1, n - 2):
                # Avoid duplicates for the second element
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                # Optimization: if the smallest possible sum is greater than target, break
                if nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target:
                    break
                # Optimization: if the largest possible sum with nums[i] and nums[j] is less than target, skip
                if nums[i] + nums[j] + nums[n - 2] + nums[n - 1] < target:
                    continue
                
                # Two-pointer approach for the remaining two elements
                left, right = j + 1, n - 1
                while left < right:
                    curr_sum = nums[i] + nums[j] + nums[left] + nums[right]
                    if curr_sum == target:
                        results.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        # Avoid duplicates for the third element
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        # Avoid duplicates for the fourth element
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                    elif curr_sum < target:
                        left += 1
                    else:
                        right -= 1
                        
        return results
```
