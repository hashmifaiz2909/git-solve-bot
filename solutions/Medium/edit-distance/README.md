# Edit Distance

**Difficulty:** Medium  
**LeetCode Link:** [Open Problem](https://leetcode.com/problems/edit-distance/)

## Problem Description
Given two strings `word1` and `word2`, return *the minimum number of operations required to convert `word1` to `word2`*.

You have the following three operations permitted on a word:

* Insert a character
* Delete a character
* Replace a character

**Example 1:**

```
Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
```

**Example 2:**

```
Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
```

**Constraints:**

* `0 <= word1.length, word2.length <= 500`
* `word1` and `word2` consist of lowercase English letters.

## Solution

- **Language:** Python3
- **Time Complexity:** O(M * N) where M and N are the lengths of word1 and word2 respectively.
- **Space Complexity:** O(M * N) to store the DP table.

### Approach
The problem is solved using Dynamic Programming. We define a 2D array `dp` where `dp[i][j]` represents the minimum number of operations to convert the prefix `word1[0...i-1]` to `word2[0...j-1]`. For each character pair, if they match, no new operation is needed, so `dp[i][j] = dp[i-1][j-1]`. If they do not match, we take the minimum of three possible operations: replace (`dp[i-1][j-1]`), delete (`dp[i-1][j]`), or insert (`dp[i][j-1]`), and add 1 to it.

### Code
```py
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j
            
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(
                        dp[i-1][j-1], # Replace
                        dp[i-1][j],   # Delete
                        dp[i][j-1]    # Insert
                    )
        return dp[m][n]
```
