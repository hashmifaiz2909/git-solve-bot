# Combination Sum

**Difficulty:** Medium  
**LeetCode Link:** [Open Problem](https://leetcode.com/problems/combination-sum/)

## Problem Description
Given an array of **distinct** integers `candidates` and a target integer `target`, return *a list of all **unique combinations** of* `candidates` *where the chosen numbers sum to* `target`*.* You may return the combinations in **any order**.

The **same** number may be chosen from `candidates` an **unlimited number of times**. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to `target` is less than `150` combinations for the given input.

**Example 1:**

```
Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.
```

**Example 2:**

```
Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]
```

**Example 3:**

```
Input: candidates = [2], target = 1
Output: []
```

**Constraints:**

* `1 <= candidates.length <= 30`
* `2 <= candidates[i] <= 40`
* All elements of `candidates` are **distinct**.
* `1 <= target <= 40`

## Solution

- **Language:** Python3
- **Time Complexity:** O(N^(T / M)) where N is the number of candidates, T is the target, and M is the minimal value among candidates. Sorting takes O(N log N).
- **Space Complexity:** O(T / M) for the recursion stack and the path array, where T is the target and M is the minimal candidate value.

### Approach
The solution uses a backtracking approach to explore all potential combinations of candidates that sum up to the target. First, the candidates array is sorted to allow early termination of loops when a candidate exceeds the remaining target sum. The backtracking function takes the current candidate index, the remaining target, and the current combination path. At each step, if the remaining target becomes 0, the current path is added to the result list. Otherwise, we iterate through the candidates starting from the current index (allowing reuse of elements) and recursively try adding each valid candidate to the path.

### Code
```py
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        
        def backtrack(start: int, remain: int, path: List[int]):
            if remain == 0:
                res.append(list(path))
                return
            for i in range(start, len(candidates)):
                if candidates[i] > remain:
                    break
                path.append(candidates[i])
                backtrack(i, remain - candidates[i], path)
                path.pop()
        
        backtrack(0, target, [])
        return res
```
