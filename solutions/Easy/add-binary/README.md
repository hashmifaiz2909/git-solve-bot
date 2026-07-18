# Add Binary

**Difficulty:** Easy  
**LeetCode Link:** [Open Problem](https://leetcode.com/problems/add-binary/)

## Problem Description
Given two binary strings `a` and `b`, return *their sum as a binary string*.

**Example 1:**

```
Input: a = "11", b = "1"
Output: "100"
```

**Example 2:**

```
Input: a = "1010", b = "1011"
Output: "10101"
```

**Constraints:**

* `1 <= a.length, b.length <= 104`
* `a` and `b` consist only of `'0'` or `'1'` characters.
* Each string does not contain leading zeros except for the zero itself.

## Solution

- **Language:** Python3
- **Time Complexity:** O(max(N, M))
- **Space Complexity:** O(max(N, M))

### Approach
The algorithm simulates the standard column-by-column addition of binary numbers from right to left. We use two pointers starting at the end of each string and a carry variable initialized to 0. In each iteration, we sum the digits at the current positions along with the carry, append the resulting bit (sum % 2) to our list, and update the carry (sum // 2). Finally, we reverse the list of bits and join them to form the final binary string.

### Code
```py
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = []
        carry = 0
        i, j = len(a) - 1, len(b) - 1
        
        while i >= 0 or j >= 0 or carry:
            total = carry
            if i >= 0:
                total += int(a[i])
                i -= 1
            if j >= 0:
                total += int(b[j])
                j -= 1
            result.append(str(total % 2))
            carry = total // 2
            
        return "".join(reversed(result))
```
