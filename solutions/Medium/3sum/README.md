# 3Sum

**Difficulty:** Medium  
**LeetCode Link:** [Open Problem](https://leetcode.com/problems/3sum/)

## Problem Description
Given an integer array nums, return all the triplets `[nums[i], nums[j], nums[k]]` such that `i != j`, `i != k`, and `j != k`, and `nums[i] + nums[j] + nums[k] == 0`.

Notice that the solution set must not contain duplicate triplets.

**Example 1:**

```
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
```

**Example 2:**

```
Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
```

**Example 3:**

```
Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
```

**Constraints:**

* `3 <= nums.length <= 3000`
* `-105 <= nums[i] <= 105`

## Solution

- **Language:** Python3
- **Time Complexity:** O(N^2), where N is the length of the array. Sorting takes O(N log N) time, and the nested two-pointer loop takes O(N^2) time.
- **Space Complexity:** O(N) for Python's built-in Timsort algorithm. The two-pointer traversal uses O(1) additional space.

### Approach
To avoid duplicate triplets and optimize search time, we first sort the array. We iterate through each element `nums[i]` as the anchor for our triplet. For each anchor, we use two pointers (`left` and `right`) starting at `i + 1` and `len(nums) - 1` respectively. If the sum of the three numbers is zero, we record the triplet and move both pointers while skipping duplicate values. If the sum is less than zero, we increment `left` to increase the sum. If the sum is greater than zero, we decrement `right` to reduce the sum. We also skip duplicate anchor values `nums[i]` to ensure uniqueness.

### Code
```py
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []
        n = len(nums)
        for i in range(n - 2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            left, right = i + 1, n - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    res.append([nums[i], nums[left], nums[right]])
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
        return res
```
