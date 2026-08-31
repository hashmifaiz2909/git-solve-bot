# Multiply Strings

**Difficulty:** Medium  
**LeetCode Link:** [Open Problem](https://leetcode.com/problems/multiply-strings/)

## Problem Description
Given two non-negative integers `num1` and `num2` represented as strings, return the product of `num1` and `num2`, also represented as a string.

**Note:** You must not use any built-in BigInteger library or convert the inputs to integer directly.

**Example 1:**

```
Input: num1 = "2", num2 = "3"
Output: "6"
```

**Example 2:**

```
Input: num1 = "123", num2 = "456"
Output: "56088"
```

**Constraints:**

* `1 <= num1.length, num2.length <= 200`
* `num1` and `num2` consist of digits only.
* Both `num1` and `num2` do not contain any leading zero, except the number `0` itself.

## Solution

- **Language:** Python3
- **Time Complexity:** O(N * M), where N is the length of `num1` and M is the length of `num2`.
- **Space Complexity:** O(N + M) to store the result digits in an array.

### Approach
The solution simulates the standard grade-school multiplication algorithm. We reverse both strings so that indices represent digit positions (units, tens, hundreds, etc.). An array of size `len(num1) + len(num2)` stores the intermediate products. For every digit pair `(i, j)`, we add their product to position `i + j`. After accumulating all products, we perform a single pass to propagate the carries forward. Finally, trailing zeros (which represent leading zeros in the result) are removed, and the remaining digits are reversed and converted to a string.

### Code
```py
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        
        m, n = len(num1), len(num2)
        res = [0] * (m + n)
        
        num1_rev = num1[::-1]
        num2_rev = num2[::-1]
        
        for i in range(m):
            for j in range(n):
                res[i + j] += int(num1_rev[i]) * int(num2_rev[j])
                
        for k in range(len(res) - 1):
            res[k + 1] += res[k] // 10
            res[k] %= 10
            
        while len(res) > 1 and res[-1] == 0:
            res.pop()
            
        return "".join(str(d) for d in res[::-1])
```
