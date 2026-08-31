# Spiral Matrix II

**Difficulty:** Medium  
**LeetCode Link:** [Open Problem](https://leetcode.com/problems/spiral-matrix-ii/)

## Problem Description
Given a positive integer `n`, generate an `n x n` `matrix` filled with elements from `1` to `n2` in spiral order.

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/11/13/spiraln.jpg)

```
Input: n = 3
Output: [[1,2,3],[8,9,4],[7,6,5]]
```

**Example 2:**

```
Input: n = 1
Output: [[1]]
```

**Constraints:**

* `1 <= n <= 20`

## Solution

- **Language:** Python3
- **Time Complexity:** O(n^2)
- **Space Complexity:** O(1)

### Approach
We maintain four boundaries: `top`, `bottom`, `left`, and `right`. Starting with `num = 1`, we traverse the matrix in a spiral order by filling the top row, right column, bottom row, and left column sequentially, shrinking the boundaries after completing each side. The loop continues until all numbers from 1 to n^2 are placed.

### Code
```py
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)]
        top, bottom = 0, n - 1
        left, right = 0, n - 1
        num = 1
        
        while top <= bottom and left <= right:
            for col in range(left, right + 1):
                matrix[top][col] = num
                num += 1
            top += 1
            
            for row in range(top, bottom + 1):
                matrix[row][right] = num
                num += 1
            right -= 1
            
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    matrix[bottom][col] = num
                    num += 1
                bottom -= 1
            
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    matrix[row][left] = num
                    num += 1
                left += 1
                
        return matrix
```
