# Generate Parentheses

**Difficulty:** Medium  
**LeetCode Link:** [Open Problem](https://leetcode.com/problems/generate-parentheses/)

## Problem Description
Given `n` pairs of parentheses, write a function to *generate all combinations of well-formed parentheses*.

**Example 1:**

```
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
```

**Example 2:**

```
Input: n = 1
Output: ["()"]
```

**Constraints:**

* `1 <= n <= 8`

## Solution

- **Language:** Python3
- **Time Complexity:** O(4^n / sqrt(n))
- **Space Complexity:** O(n)

### Approach
We use a recursive backtracking approach to build valid parentheses combinations step-by-step. We keep track of the number of open and close parentheses used. An open parenthesis '(' can be added if open_count < n. A close parenthesis ')' can be added if close_count < open_count, ensuring the expression remains valid. Once the string reaches length 2 * n, it is added to the result list.

### Code
```py
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(s: str, open_count: int, close_count: int):
            if len(s) == 2 * n:
                res.append(s)
                return
            if open_count < n:
                backtrack(s + '(', open_count + 1, close_count)
            if close_count < open_count:
                backtrack(s + ')', open_count, close_count + 1)
        
        backtrack("", 0, 0)
        return res
```
