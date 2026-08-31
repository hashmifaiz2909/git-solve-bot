# Unique Paths II

**Difficulty:** Medium  
**LeetCode Link:** [Open Problem](https://leetcode.com/problems/unique-paths-ii/)

## Problem Description
You are given an `m x n` integer array `grid`. There is a robot initially located at the **top-left corner** (i.e., `grid[0][0]`). The robot tries to move to the **bottom-right corner** (i.e., `grid[m - 1][n - 1]`). The robot can only move either down or right at any point in time.

An obstacle and space are marked as `1` or `0` respectively in `grid`. A path that the robot takes cannot include **any** square that is an obstacle.

Return *the number of possible unique paths that the robot can take to reach the bottom-right corner*.

The testcases are generated so that the answer will be less than or equal to `2 * 109`.

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/11/04/robot1.jpg)

```
Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
Output: 2
Explanation: There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right
```

**Example 2:**

![](https://assets.leetcode.com/uploads/2020/11/04/robot2.jpg)

```
Input: obstacleGrid = [[0,1],[0,0]]
Output: 1
```

**Constraints:**

* `m == obstacleGrid.length`
* `n == obstacleGrid[i].length`
* `1 <= m, n <= 100`
* `obstacleGrid[i][j]` is `0` or `1`.

## Solution

- **Language:** Python3
- **Time Complexity:** O(m * n) where m is the number of rows and n is the number of columns, as we iterate through each cell of the grid exactly once.
- **Space Complexity:** O(n) where n is the number of columns, as we only maintain a 1D array of size n to store the DP states.

### Approach
The problem can be solved using dynamic programming. We define a 1D array `dp` of size `n` (the number of columns) to store the number of unique paths to reach each cell in the current row. We initialize `dp[0] = 1` because there is only 1 way to start at the top-left corner (if it is not an obstacle). For each cell `(i, j)` in the grid, if it contains an obstacle, we set `dp[j] = 0` because no paths can pass through it. Otherwise, the number of paths to reach `(i, j)` is the sum of the paths from the top `(i-1, j)` (which is already stored in `dp[j]`) and the paths from the left `(i, j-1)` (which is stored in `dp[j-1]`). We update `dp[j]` in-place to optimize space complexity.

### Code
```py
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid or not obstacleGrid[0] or obstacleGrid[0][0] == 1:
            return 0
        
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [0] * n
        dp[0] = 1
        
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    dp[j] = 0
                elif j > 0:
                    dp[j] += dp[j-1]
                    
        return dp[-1]
```
