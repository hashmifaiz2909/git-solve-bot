# Sudoku Solver

**Difficulty:** Hard  
**LeetCode Link:** [Open Problem](https://leetcode.com/problems/sudoku-solver/)

## Problem Description
Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy **all of the following rules**:

1. Each of the digits `1-9` must occur exactly once in each row.
2. Each of the digits `1-9` must occur exactly once in each column.
3. Each of the digits `1-9` must occur exactly once in each of the 9 `3x3` sub-boxes of the grid.

The `'.'` character indicates empty cells.

**Example 1:**

![](https://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Sudoku-by-L2G-20050714.svg/250px-Sudoku-by-L2G-20050714.svg.png)

```
Input: board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
Output: [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
Explanation: The input board is shown above and the only valid solution is shown below:

![](https://upload.wikimedia.org/wikipedia/commons/thumb/3/31/Sudoku-by-L2G-20050714_solution.svg/250px-Sudoku-by-L2G-20050714_solution.svg.png)
```

**Constraints:**

* `board.length == 9`
* `board[i].length == 9`
* `board[i][j]` is a digit or `'.'`.
* It is **guaranteed** that the input board has only one solution.

## Solution

- **Language:** Python3
- **Time Complexity:** O(9^N) worst-case, where N is the number of empty cells, but significantly faster in practice due to bitmask state tracking and MRV pruning.
- **Space Complexity:** O(N) for recursion stack and tracking empty cells, where N <= 81.

### Approach
The solution uses backtracking optimized with bitmasks and the Minimum Remaining Values (MRV) heuristic. Bitmasks for each row, column, and 3x3 box track used numbers efficiently using bitwise operations. At each step of the recursion, the solver picks the empty cell with the fewest valid candidate numbers available to minimize branching (MRV heuristic). Bit manipulation operations (`best_mask & -best_mask`) iterate over available numbers rapidly.

### Code
```py
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = [0] * 9
        cols = [0] * 9
        boxes = [0] * 9
        empty = []

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    empty.append((r, c))
                else:
                    digit = int(board[r][c]) - 1
                    mask = 1 << digit
                    rows[r] |= mask
                    cols[c] |= mask
                    boxes[(r // 3) * 3 + c // 3] |= mask

        def backtrack(empty_idx: int) -> bool:
            if empty_idx == len(empty):
                return True

            best_i = empty_idx
            min_choices = 10
            best_mask = 0

            for i in range(empty_idx, len(empty)):
                r, c = empty[i]
                b = (r // 3) * 3 + c // 3
                mask = 0x1FF & ~(rows[r] | cols[c] | boxes[b])
                choices = bin(mask).count('1')
                if choices < min_choices:
                    min_choices = choices
                    best_i = i
                    best_mask = mask
                if min_choices == 0:
                    break

            if min_choices == 0:
                return False

            empty[empty_idx], empty[best_i] = empty[best_i], empty[empty_idx]
            r, c = empty[empty_idx]
            b = (r // 3) * 3 + c // 3

            while best_mask:
                lsb = best_mask & -best_mask
                digit = lsb.bit_length() - 1

                board[r][c] = str(digit + 1)
                rows[r] |= lsb
                cols[c] |= lsb
                boxes[b] |= lsb

                if backtrack(empty_idx + 1):
                    return True

                rows[r] ^= lsb
                cols[c] ^= lsb
                boxes[b] ^= lsb
                board[r][c] = '.'
                best_mask &= best_mask - 1

            empty[empty_idx], empty[best_i] = empty[best_i], empty[empty_idx]
            return False

        backtrack(0)
```
