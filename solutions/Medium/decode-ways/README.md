# Decode Ways

**Difficulty:** Medium  
**LeetCode Link:** [Open Problem](https://leetcode.com/problems/decode-ways/)

## Problem Description
You have intercepted a secret message encoded as a string of numbers. The message is **decoded** via the following mapping:

`"1" -> 'A'  
"2" -> 'B'  
...  
"25" -> 'Y'  
"26" -> 'Z'`

However, while decoding the message, you realize that there are many different ways you can decode the message because some codes are contained in other codes (`"2"` and `"5"` vs `"25"`).

For example, `"11106"` can be decoded into:

* `"AAJF"` with the grouping `(1, 1, 10, 6)`
* `"KJF"` with the grouping `(11, 10, 6)`
* The grouping `(1, 11, 06)` is invalid because `"06"` is not a valid code (only `"6"` is valid).

Note: there may be strings that are impossible to decode.  
  
Given a string s containing only digits, return the **number of ways** to **decode** it. If the entire string cannot be decoded in any valid way, return `0`.

The test cases are generated so that the answer fits in a **32-bit** integer.

**Example 1:**

**Input:** s = "12"

**Output:** 2

**Explanation:**

"12" could be decoded as "AB" (1 2) or "L" (12).

**Example 2:**

**Input:** s = "226"

**Output:** 3

**Explanation:**

"226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

**Example 3:**

**Input:** s = "06"

**Output:** 0

**Explanation:**

"06" cannot be mapped to "F" because of the leading zero ("6" is different from "06"). In this case, the string is not a valid encoding, so return 0.

**Constraints:**

* `1 <= s.length <= 100`
* `s` contains only digits and may contain leading zero(s).

## Solution

- **Language:** Python3
- **Time Complexity:** O(N)
- **Space Complexity:** O(1)

### Approach
The problem can be solved using dynamic programming. Let dp[i] represent the number of ways to decode the prefix of string s of length i. For each character, we can either decode it as a single digit (if it is not '0') or combine it with the previous digit to form a two-digit number (if the combined value is between 10 and 26). Since we only need the results of the last two states (dp[i-1] and dp[i-2]) to compute the current state, we can optimize the space complexity to O(1) by using two variables, prev1 and prev2.

### Code
```py
class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0
        
        n = len(s)
        prev2 = 1
        prev1 = 1
        
        for i in range(2, n + 1):
            current = 0
            # Single digit decode
            if s[i-1] != '0':
                current += prev1
            # Two digit decode
            two_digit = int(s[i-2:i])
            if 10 <= two_digit <= 26:
                current += prev2
            
            prev2 = prev1
            prev1 = current
            
        return prev1
```
