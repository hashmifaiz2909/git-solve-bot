# 3Sum Closest

**Difficulty:** Medium  
**LeetCode Link:** [Open Problem](https://leetcode.com/problems/3sum-closest/)

## Problem Description
Given an integer array `nums` of length `n` and an integer `target`, find three integers at **distinct indices** in `nums` such that the sum is closest to `target`.

Return *the sum of the three integers*.

You may assume that each input would have exactly one solution.

**Example 1:**

```
Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
```

**Example 2:**

```
Input: nums = [0,0,0], target = 1
Output: 0
Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
```

**Constraints:**

* `3 <= nums.length <= 500`
* `-1000 <= nums[i] <= 1000`
* `-104 <= target <= 104`

## Solution

- **Language:** Python3
- **Time Complexity:** O(N^2) where N is the length of nums. Sorting takes O(N log N) time, and the nested loops (an outer loop of size N and an inner two-pointer scan of size N) take O(N^2) time.
- **Space Complexity:** O(N) due to Python's Timsort algorithm, which requires O(N) auxiliary space for sorting.

### Approach
The algorithm first sorts the input array. It then iterates through the array, fixing the first element of the triplet (`nums[i]`). For the remaining two elements, a two-pointer technique (`left` starting at `i + 1` and `right` starting at `n - 1`) is used to find a sum closest to the target. If the current sum is less than the target, `left` is incremented to increase the sum; if greater, `right` is decremented to decrease the sum. If an exact match to the target is found, it is returned immediately. Throughout the process, the closest sum encountered is tracked and finally returned.

### Code
```py
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        closest_sum = float('inf')
        
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, n - 1
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                if current_sum == target:
                    return target
                
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum
                
                if current_sum < target:
                    left += 1
                else:
                    right -= 1
                    
        return closest_sum
```
