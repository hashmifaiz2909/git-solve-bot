# Subsets II

**Difficulty:** Medium  
**LeetCode Link:** [Open Problem](https://leetcode.com/problems/subsets-ii/)

## Problem Description
Given an integer array `nums` that may contain duplicates, return *all possible* *subsets* *(the power set)*.

The solution set **must not** contain duplicate subsets. Return the solution in **any order**.

**Example 1:**

```
Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
```

**Example 2:**

```
Input: nums = [0]
Output: [[],[0]]
```

**Constraints:**

* `1 <= nums.length <= 10`
* `-10 <= nums[i] <= 10`

## Solution

- **Language:** Python3
- **Time Complexity:** O(N * 2^N)
- **Space Complexity:** O(N)

### Approach
To avoid duplicate subsets, we first sort the input array `nums`. This groups identical elements together. We then use a backtracking algorithm to generate all subsets. During the backtracking process, at each step, we iterate through the remaining elements. If the current element is the same as the previous element and we are not at the starting index of the current recursion level, we skip it to prevent generating duplicate subsets. This ensures that each unique combination of elements is generated exactly once.

### Code
```py
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        
        def backtrack(start: int, path: List[int]):
            res.append(list(path))
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()
                
        backtrack(0, [])
        return res
```
