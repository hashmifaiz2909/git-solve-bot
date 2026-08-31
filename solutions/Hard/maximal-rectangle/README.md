# Maximal Rectangle

**Difficulty:** Hard  
**LeetCode Link:** [Open Problem](https://leetcode.com/problems/maximal-rectangle/)

## Problem Description
Given a `rows x cols` binary `matrix` filled with `0`'s and `1`'s, find the largest rectangle containing only `1`'s and return *its area*.

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/09/14/maximal.jpg)

```
Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 6
Explanation: The maximal rectangle is shown in the above picture.
```

**Example 2:**

```
Input: matrix = [["0"]]
Output: 0
```

**Example 3:**

```
Input: matrix = [["1"]]
Output: 1
```

**Constraints:**

* `rows == matrix.length`
* `cols == matrix[i].length`
* `1 <= rows, cols <= 200`
* `matrix[i][j]` is `'0'` or `'1'`.

## Solution

- **Language:** Python3
- **Time Complexity:** O(R * C) where R is the number of rows and C is the number of columns in the matrix.
- **Space Complexity:** O(C) to store the heights array and the monotonic stack.

### Approach
The problem can be reduced to finding the 'Largest Rectangle in Histogram' for each row of the matrix. We maintain an array `heights` of size equal to the number of columns. As we iterate through each row, we update `heights[c]` to be `heights[c] + 1` if `matrix[r][c] == '1'`, or reset it to `0` if `matrix[r][c] == '0'`. For each row, we then apply the monotonic stack algorithm to find the largest rectangle in the histogram represented by the updated `heights` in O(C) time. The overall maximum area found across all rows is our answer.

### Code
```py
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        
        cols = len(matrix[0])
        heights = [0] * cols
        max_area = 0
        
        for row in matrix:
            for c in range(cols):
                if row[c] == '1':
                    heights[c] += 1
                else:
                    heights[c] = 0
            
            # Calculate the maximum rectangle in the histogram for the current row
            stack = []
            extended_heights = heights + [0]
            for i, h in enumerate(extended_heights):
                while stack and extended_heights[stack[-1]] > h:
                    height_idx = stack.pop()
                    height = extended_heights[height_idx]
                    width = i if not stack else i - stack[-1] - 1
                    max_area = max(max_area, height * width)
                stack.append(i)
                
        return max_area
```
