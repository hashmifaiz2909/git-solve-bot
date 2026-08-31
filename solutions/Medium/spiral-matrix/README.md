# Spiral Matrix

**Difficulty:** Medium  
**LeetCode Link:** [Open Problem](https://leetcode.com/problems/spiral-matrix/)

## Problem Description
Given an `m x n` `matrix`, return *all elements of the* `matrix` *in spiral order*.

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/11/13/spiral1.jpg)

```
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
```

**Example 2:**

![](https://assets.leetcode.com/uploads/2020/11/13/spiral.jpg)

```
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
```

**Constraints:**

* `m == matrix.length`
* `n == matrix[i].length`
* `1 <= m, n <= 10`
* `-100 <= matrix[i][j] <= 100`

## Solution

- **Language:** Python3
- **Time Complexity:** O(m * n) where m is the number of rows and n is the number of columns, because every element in the matrix is visited exactly once.
- **Space Complexity:** O(1) auxiliary space, excluding the space required for the output array.

### Approach
We define four boundaries: top, bottom, left, and right. We simulate the spiral traversal by iteratively visiting elements from left to right along the top boundary, top to bottom along the right boundary, right to left along the bottom boundary, and bottom to top along the left boundary. After traversing each side, we shrink the corresponding boundary inward. We stop when the boundaries overlap.

### Code
```py
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        
        result = []
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1
        
        while top <= bottom and left <= right:
            # Traverse Right
            for c in range(left, right + 1):
                result.append(matrix[top][c])
            top += 1
            
            # Traverse Down
            for r in range(top, bottom + 1):
                result.append(matrix[r][right])
            right -= 1
            
            # Traverse Left
            if top <= bottom:
                for c in range(right, left - 1, -1):
                    result.append(matrix[bottom][c])
                bottom -= 1
            
            # Traverse Up
            if left <= right:
                for r in range(bottom, top - 1, -1):
                    result.append(matrix[r][left])
                left += 1
                
        return result
```
