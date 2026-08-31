# Combination Sum II

**Difficulty:** Medium  
**LeetCode Link:** [Open Problem](https://leetcode.com/problems/combination-sum-ii/)

## Problem Description
Given a collection of candidate numbers (`candidates`) and a target number (`target`), find all unique combinations in `candidates` where the candidate numbers sum to `target`.

Each number in `candidates` may only be used **once** in the combination.

**Note:** The solution set must not contain duplicate combinations.

**Example 1:**

```
Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
```

**Example 2:**

```
Input: candidates = [2,5,2,1,2], target = 5
Output: 
[
[1,2,2],
[5]
]
```

**Constraints:**

* `1 <= candidates.length <= 100`
* `1 <= candidates[i] <= 50`
* `1 <= target <= 30`

## Solution

- **Language:** Python3
- **Time Complexity:** O(2^N)
- **Space Complexity:** O(N)

### Approach
To find all unique combinations summing up to the target, we use backtracking after sorting the candidates list. Sorting helps in two ways: it allows us to break early from the loop when a candidate exceeds the remaining target, and it groups identical elements together. During backtracking, if an element is equal to the previous element at the same recursion depth (i.e., `i > start` and `candidates[i] == candidates[i - 1]`), we skip it to prevent generating duplicate combinations.

### Code
```py
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        results = []
        
        def backtrack(start: int, remaining: int, path: List[int]):
            if remaining == 0:
                results.append(list(path))
                return
            
            for i in range(start, len(candidates)):
                if candidates[i] > remaining:
                    break
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                
                path.append(candidates[i])
                backtrack(i + 1, remaining - candidates[i], path)
                path.pop()
                
        backtrack(0, target, [])
        return results
```
