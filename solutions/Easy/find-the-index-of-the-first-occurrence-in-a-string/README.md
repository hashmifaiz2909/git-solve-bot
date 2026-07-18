# Find the Index of the First Occurrence in a String

**Difficulty:** Easy  
**LeetCode Link:** [Open Problem](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/)

## Problem Description
Given two strings `needle` and `haystack`, return the index of the first occurrence of `needle` in `haystack`, or `-1` if `needle` is not part of `haystack`.

**Example 1:**

```
Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
```

**Example 2:**

```
Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
```

**Constraints:**

* `1 <= haystack.length, needle.length <= 104`
* `haystack` and `needle` consist of only lowercase English characters.

## Solution

- **Language:** Python3
- **Time Complexity:** O(N + M) where N is the length of haystack and M is the length of needle.
- **Space Complexity:** O(M) to store the LPS array of size M.

### Approach
The solution uses the Knuth-Morris-Pratt (KMP) string matching algorithm. First, we construct the Longest Prefix Suffix (LPS) array for the `needle` string, which helps us avoid redundant comparisons by determining how many characters we can skip matching after a mismatch. Then, we traverse the `haystack` using the LPS array to find the first occurrence of the `needle` in linear time.

### Code
```py
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        
        # KMP Algorithm
        # Step 1: Build the LPS (Longest Prefix Suffix) array
        lps = [0] * len(needle)
        prevLPS, i = 0, 1
        while i < len(needle):
            if needle[i] == needle[prevLPS]:
                lps[i] = prevLPS + 1
                prevLPS += 1
                i += 1
            else:
                if prevLPS == 0:
                    lps[i] = 0
                    i += 1
                else:
                    prevLPS = lps[prevLPS - 1]
        
        # Step 2: Search the needle in the haystack
        i = 0  # index for haystack
        j = 0  # index for needle
        while i < len(haystack):
            if haystack[i] == needle[j]:
                i += 1
                j += 1
            else:
                if j == 0:
                    i += 1
                else:
                    j = lps[j - 1]
            
            if j == len(needle):
                return i - len(needle)
        
        return -1
```
