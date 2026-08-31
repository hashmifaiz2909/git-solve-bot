# Combinations

**Difficulty:** Medium  
**LeetCode Link:** [Open Problem](https://leetcode.com/problems/combinations/)

## Problem Description
Given two integers `n` and `k`, return *all possible combinations of* `k` *numbers chosen from the range* `[1, n]`.

You may return the answer in **any order**.

**Example 1:**

```
Input: n = 4, k = 2
Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
Explanation: There are 4 choose 2 = 6 total combinations.
Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.
```

**Example 2:**

```
Input: n = 1, k = 1
Output: [[1]]
Explanation: There is 1 choose 1 = 1 total combination.
```

**Constraints:**

* `1 <= n <= 20`
* `1 <= k <= n`

## Solution

- **Language:** Python3
- **Time Complexity:** O(k * C(n, k)) where C(n, k) is the number of combinations, because there are C(n, k) combinations and we spend O(k) time to copy each combination into the result list.
- **Space Complexity:** O(k) auxiliary space for the recursion stack and the path list (excluding the space required for the output list).

### Approach
The problem is solved using backtracking. We recursively build combinations of size `k` from the range `[1, n]`. To optimize the search, we apply pruning: at any point, if the number of remaining elements we need to choose (`k - len(path)`) is greater than the number of available elements in the range (`n - i + 1`), we stop exploring that branch. This significantly reduces the number of unnecessary recursive calls.

### Code
```py
from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        def backtrack(start: int, path: List[int]):
            if len(path) == k:
                result.append(list(path))
                return
            
            # Pruning: only loop if there are enough remaining elements to form a combination of size k
            for i in range(start, n - (k - len(path)) + 2):
                path.append(i)
                backtrack(i + 1, path)
                path.pop()
                
        backtrack(1, [])
        return result
```
