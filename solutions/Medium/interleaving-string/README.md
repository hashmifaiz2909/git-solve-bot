# Interleaving String

**Difficulty:** Medium  
**LeetCode Link:** [Open Problem](https://leetcode.com/problems/interleaving-string/)

## Problem Description
Given strings `s1`, `s2`, and `s3`, find whether `s3` is formed by an **interleaving** of `s1` and `s2`.

An **interleaving** of two strings `s` and `t` is a configuration where `s` and `t` are divided into `n` and `m` substrings respectively, such that:

* `s = s1 + s2 + ... + sn`
* `t = t1 + t2 + ... + tm`
* `|n - m| <= 1`
* The **interleaving** is `s1 + t1 + s2 + t2 + s3 + t3 + ...` or `t1 + s1 + t2 + s2 + t3 + s3 + ...`

**Note:** `a + b` is the concatenation of strings `a` and `b`.

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/09/02/interleave.jpg)

```
Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true
Explanation: One way to obtain s3 is:
Split s1 into s1 = "aa" + "bc" + "c", and s2 into s2 = "dbbc" + "a".
Interleaving the two splits, we get "aa" + "dbbc" + "bc" + "a" + "c" = "aadbbcbcac".
Since s3 can be obtained by interleaving s1 and s2, we return true.
```

**Example 2:**

```
Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false
Explanation: Notice how it is impossible to interleave s2 with any other string to obtain s3.
```

**Example 3:**

```
Input: s1 = "", s2 = "", s3 = ""
Output: true
```

**Constraints:**

* `0 <= s1.length, s2.length <= 100`
* `0 <= s3.length <= 200`
* `s1`, `s2`, and `s3` consist of lowercase English letters.

**Follow up:** Could you solve it using only `O(s2.length)` additional memory space?

## Solution

- **Language:** Python3
- **Time Complexity:** O(N * M) where N is the length of s1 and M is the length of s2.
- **Space Complexity:** O(min(N, M)) as we only maintain a 1D DP array of size min(N, M) + 1.

### Approach
The problem can be solved using Dynamic Programming. We define a 1D DP array `dp` of size `len(s2) + 1`, where `dp[j]` represents whether `s3[0...i+j-1]` can be formed by interleaving `s1[0...i-1]` and `s2[0...j-1]`. We initialize the DP array for the base case where `s1` is empty. Then, we iterate through each character of `s1` and update the DP array. For each state, `dp[j]` is updated to `True` if either the current character of `s1` matches `s3` and the previous state `dp[j]` (from the previous row) was `True`, or the current character of `s2` matches `s3` and the previous state `dp[j-1]` (from the current row) was `True`. To optimize space, we swap `s1` and `s2` if `len(s1) < len(s2)` so that the DP array size is `O(min(len(s1), len(s2)))`.

### Code
```py
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        
        # Ensure s2 is the shorter string to optimize space complexity to O(min(len(s1), len(s2)))
        if len(s1) < len(s2):
            s1, s2 = s2, s1
            
        n, m = len(s1), len(s2)
        dp = [False] * (m + 1)
        
        # Base case: empty s1 and empty s2
        dp[0] = True
        
        # Initialize DP for i = 0 (only using characters from s2)
        for j in range(1, m + 1):
            dp[j] = dp[j - 1] and s2[j - 1] == s3[j - 1]
            
        # Fill the DP table row by row
        for i in range(1, n + 1):
            dp[0] = dp[0] and s1[i - 1] == s3[i - 1]
            for j in range(1, m + 1):
                dp[j] = (dp[j] and s1[i - 1] == s3[i + j - 1]) or (dp[j - 1] and s2[j - 1] == s3[i + j - 1])
                
        return dp[m]
```
