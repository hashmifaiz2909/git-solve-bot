# Permutations

**Difficulty:** Medium  
**LeetCode Link:** [Open Problem](https://leetcode.com/problems/permutations/)

## Problem Description
Given an array `nums` of distinct integers, return all the possible permutations. You can return the answer in **any order**.

**Example 1:**

```
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
```

**Example 2:**

```
Input: nums = [0,1]
Output: [[0,1],[1,0]]
```

**Example 3:**

```
Input: nums = [1]
Output: [[1]]
```

**Constraints:**

* `1 <= nums.length <= 6`
* `-10 <= nums[i] <= 10`
* All the integers of `nums` are **unique**.

## Solution

- **Language:** Python3
- **Time Complexity:** O(N * N!) where N is the length of nums. There are N! permutations, and creating a copy of each permutation takes O(N) time.
- **Space Complexity:** O(N) for the recursion stack depth (excluding the output list required to store all permutations).

### Approach
We use a backtracking algorithm to generate all permutations. The algorithm works by placing each candidate integer at the `first` position of the current permutation, recursively building the rest of the permutation for positions `first + 1` to `n - 1`, and then backtracking by swapping the elements back to restore the array state.

### Code
```py
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(first=0):
            if first == n:
                res.append(nums[:])
                return
            for i in range(first, n):
                nums[first], nums[i] = nums[i], nums[first]
                backtrack(first + 1)
                nums[first], nums[i] = nums[i], nums[first]

        n = len(nums)
        res = []
        backtrack()
        return res
```
