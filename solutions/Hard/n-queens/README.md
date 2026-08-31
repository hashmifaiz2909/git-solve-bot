# N-Queens

**Difficulty:** Hard  
**LeetCode Link:** [Open Problem](https://leetcode.com/problems/n-queens/)

## Problem Description
The **n-queens** puzzle is the problem of placing `n` queens on an `n x n` chessboard such that no two queens attack each other.

Given an integer `n`, return *all distinct solutions to the **n-queens puzzle***. You may return the answer in **any order**.

Each solution contains a distinct board configuration of the n-queens' placement, where `'Q'` and `'.'` both indicate a queen and an empty space, respectively.

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/11/13/queens.jpg)

```
Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above
```

**Example 2:**

```
Input: n = 1
Output: [["Q"]]
```

**Constraints:**

* `1 <= n <= 9`

## Solution

- **Language:** Python3
- **Time Complexity:** O(N!)
- **Space Complexity:** O(N)

### Approach
The problem is solved using backtracking. We place queens row by row. For each row, we attempt to place a queen in a column that does not conflict with already placed queens. To check for conflicts efficiently, we maintain three sets: 'cols' for columns, 'diag1' for major diagonals (where row - col is constant), and 'diag2' for minor diagonals (where row + col is constant). If a valid position is found, we place the queen, proceed to the next row, and backtrack by removing the queen to explore other possibilities. Once a valid configuration of N queens is found, we format the board and add it to the results.

### Code
```py
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        cols = set()
        diag1 = set()  # row - col
        diag2 = set()  # row + col
        board = []
        
        def backtrack(row):
            if row == n:
                ans.append(["." * col + "Q" + "." * (n - col - 1) for col in board])
                return
            
            for col in range(n):
                if col in cols or (row - col) in diag1 or (row + col) in diag2:
                    continue
                
                cols.add(col)
                diag1.add(row - col)
                diag2.add(row + col)
                board.append(col)
                
                backtrack(row + 1)
                
                cols.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)
                board.pop()
        
        backtrack(0)
        return ans
```
