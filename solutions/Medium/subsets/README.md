# Subsets

**Difficulty:** Medium  
**LeetCode Link:** [Open Problem](https://leetcode.com/problems/subsets/)

## Problem Description
Given an integer array `nums` of **unique** elements, return *all possible* *subsets* *(the power set)*.

The solution set **must not** contain duplicate subsets. Return the solution in **any order**.

**Example 1:**

```
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
```

**Example 2:**

```
Input: nums = [0]
Output: [[],[0]]
```

**Constraints:**

* `1 <= nums.length <= 10`
* `-10 <= nums[i] <= 10`
* All the numbers of `nums` are **unique**.

## Solution

- **Language:** Python3
- **Time Complexity:** O(N * 2^N)
- **Space Complexity:** O(N * 2^N)

### Approach
We use an iterative approach to construct the power set. Starting with a list containing just the empty subset `[[]]`, we process each number in `nums` one by one. For every number, we take all existing subsets in our result, create new subsets by appending the current number to each of them, and add these new subsets to our result. Because all elements in `nums` are unique, this guarantees all $2^N$ generated subsets are unique.

### Code
```py
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for num in nums:
            res += [curr + [num] for curr in res]
        return res
```
