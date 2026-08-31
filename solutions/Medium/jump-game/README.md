# Jump Game

**Difficulty:** Medium  
**LeetCode Link:** [Open Problem](https://leetcode.com/problems/jump-game/)

## Problem Description
You are given an integer array `nums`. You are initially positioned at the array's **first index**, and each element in the array represents your maximum jump length at that position.

Return `true` *if you can reach the last index, or* `false` *otherwise*.

**Example 1:**

```
Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
```

**Example 2:**

```
Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
```

**Constraints:**

* `1 <= nums.length <= 104`
* `0 <= nums[i] <= 105`

## Solution

- **Language:** Python3
- **Time Complexity:** O(N)
- **Space Complexity:** O(1)

### Approach
We use a greedy approach to keep track of the maximum reachable index from the current position (`max_reachable`). We iterate through the array: if the current index `i` exceeds `max_reachable`, it means we cannot reach this point, so we return `False`. Otherwise, we update `max_reachable` to be `max(max_reachable, i + nums[i])`. If `max_reachable` reaches or exceeds the last index at any point, we can immediately return `True`.

### Code
```py
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reachable = 0
        for i, jump in enumerate(nums):
            if i > max_reachable:
                return False
            max_reachable = max(max_reachable, i + jump)
            if max_reachable >= len(nums) - 1:
                return True
        return True
```
