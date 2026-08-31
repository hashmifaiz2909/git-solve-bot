# Scramble String

**Difficulty:** Hard  
**LeetCode Link:** [Open Problem](https://leetcode.com/problems/scramble-string/)

## Problem Description
We can scramble a string s to get a string t using the following algorithm:

1. If the length of the string is 1, stop.
2. If the length of the string is > 1, do the following:
   * Split the string into two non-empty substrings at a random index, i.e., if the string is `s`, divide it to `x` and `y` where `s = x + y`.
   * **Randomly** decide to swap the two substrings or to keep them in the same order. i.e., after this step, `s` may become `s = x + y` or `s = y + x`.
   * Apply step 1 recursively on each of the two substrings `x` and `y`.

Given two strings `s1` and `s2` of **the same length**, return `true` if `s2` is a scrambled string of `s1`, otherwise, return `false`.

**Example 1:**

```
Input: s1 = "great", s2 = "rgeat"
Output: true
Explanation: One possible scenario applied on s1 is:
"great" --> "gr/eat" // divide at random index.
"gr/eat" --> "gr/eat" // random decision is not to swap the two substrings and keep them in order.
"gr/eat" --> "g/r / e/at" // apply the same algorithm recursively on both substrings. divide at random index each of them.
"g/r / e/at" --> "r/g / e/at" // random decision was to swap the first substring and to keep the second substring in the same order.
"r/g / e/at" --> "r/g / e/ a/t" // again apply the algorithm recursively, divide "at" to "a/t".
"r/g / e/ a/t" --> "r/g / e/ a/t" // random decision is to keep both substrings in the same order.
The algorithm stops now, and the result string is "rgeat" which is s2.
As one possible scenario led s1 to be scrambled to s2, we return true.
```

**Example 2:**

```
Input: s1 = "abcde", s2 = "caebd"
Output: false
```

**Example 3:**

```
Input: s1 = "a", s2 = "a"
Output: true
```

**Constraints:**

* `s1.length == s2.length`
* `1 <= s1.length <= 30`
* `s1` and `s2` consist of lowercase English letters.

## Solution

- **Language:** Python3
- **Time Complexity:** O(N^4) where N is the length of the strings. There are O(N^3) states, and for each state, we perform a loop of size up to N and string operations of size up to N.
- **Space Complexity:** O(N^3) to store the memoization table of states, and O(N) for the recursion stack.

### Approach
The problem is solved using top-down dynamic programming (memoized recursion). We define a recursive function `dfs(i1, i2, length)` which checks if the substring of `s1` starting at `i1` of length `length` is a scramble of the substring of `s2` starting at `i2` of the same length. To optimize, we use a memoization table to store already computed states. Additionally, we apply a powerful pruning step: if the sorted characters of the two substrings do not match, they cannot be scrambled versions of each other, allowing us to return `False` early.

### Code
```py
class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        memo = {}
        
        def dfs(i1, i2, length):
            state = (i1, i2, length)
            if state in memo:
                return memo[state]
            
            sub1 = s1[i1:i1+length]
            sub2 = s2[i2:i2+length]
            
            if sub1 == sub2:
                memo[state] = True
                return True
            
            # Pruning: If the sorted characters of the two substrings do not match,
            # they cannot be scrambled versions of each other.
            if sorted(sub1) != sorted(sub2):
                memo[state] = False
                return False
            
            for i in range(1, length):
                # Case 1: No swap at the current split point
                if dfs(i1, i2, i) and dfs(i1 + i, i2 + i, length - i):
                    memo[state] = True
                    return True
                # Case 2: Swap at the current split point
                if dfs(i1, i2 + length - i, i) and dfs(i1 + i, i2, length - i):
                    memo[state] = True
                    return True
            
            memo[state] = False
            return False
        
        return dfs(0, 0, len(s1))
```
