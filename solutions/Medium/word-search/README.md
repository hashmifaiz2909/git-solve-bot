# Word Search

**Difficulty:** Medium  
**LeetCode Link:** [Open Problem](https://leetcode.com/problems/word-search/)

## Problem Description
Given an `m x n` grid of characters `board` and a string `word`, return `true` *if* `word` *exists in the grid*.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/11/04/word2.jpg)

```
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
```

**Example 2:**

![](https://assets.leetcode.com/uploads/2020/11/04/word-1.jpg)

```
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true
```

**Example 3:**

![](https://assets.leetcode.com/uploads/2020/10/15/word3.jpg)

```
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false
```

**Constraints:**

* `m == board.length`
* `n = board[i].length`
* `1 <= m, n <= 6`
* `1 <= word.length <= 15`
* `board` and `word` consists of only lowercase and uppercase English letters.

**Follow up:** Could you use search pruning to make your solution faster with a larger `board`?

## Solution

- **Language:** Python3
- **Time Complexity:** O(N * 3^L), where N is the total number of cells in the grid (m * n) and L is the length of the word. In the worst case, for each cell, we explore up to 3 directions for each character of the word.
- **Space Complexity:** O(L), where L is the length of the word, due to the call stack depth required for the recursion.

### Approach
The problem is solved using a Depth-First Search (DFS) with backtracking. To optimize performance, two pruning techniques are applied:
1. **Frequency Check**: We compare the character counts of `word` with `board`. If any character in `word` appears more times than it exists in the grid, we return `False` immediately.
2. **Search Optimization**: If the starting character of `word` occurs more frequently in the grid than the ending character, we reverse `word` to start searching from the less frequent character end, reducing the branching factor during early DFS stages.

During DFS, visited cells are temporarily replaced with `#` to avoid reusing characters and restored upon backtracking.

### Code
```py
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        R, C = len(board), len(board[0])
        
        # Pruning 1: Check if the grid has enough of each character required by word
        board_counts = Counter(char for row in board for char in row)
        word_counts = Counter(word)
        for char, count in word_counts.items():
            if board_counts[char] < count:
                return False
        
        # Pruning 2: Start search from the end with fewer matching characters in board
        if board_counts[word[0]] > board_counts[word[-1]]:
            word = word[::-1]
            
        def dfs(r: int, c: int, idx: int) -> bool:
            if idx == len(word):
                return True
            if r < 0 or r >= R or c < 0 or c >= C or board[r][c] != word[idx]:
                return False
            
            temp = board[r][c]
            board[r][c] = '#'
            
            res = (dfs(r + 1, c, idx + 1) or
                   dfs(r - 1, c, idx + 1) or
                   dfs(r, c + 1, idx + 1) or
                   dfs(r, c - 1, idx + 1))
                   
            board[r][c] = temp
            return res
        
        for r in range(R):
            for c in range(C):
                if board[r][c] == word[0] and dfs(r, c, 0):
                    return True
                    
        return False
```
