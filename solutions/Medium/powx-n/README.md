# Pow(x, n)

**Difficulty:** Medium  
**LeetCode Link:** [Open Problem](https://leetcode.com/problems/powx-n/)

## Problem Description
Implement [pow(x, n)](http://www.cplusplus.com/reference/valarray/pow/), which calculates `x` raised to the power `n` (i.e., `xn`).

**Example 1:**

```
Input: x = 2.00000, n = 10
Output: 1024.00000
```

**Example 2:**

```
Input: x = 2.10000, n = 3
Output: 9.26100
```

**Example 3:**

```
Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
```

**Constraints:**

* `-100.0 < x < 100.0`
* `-231 <= n <= 231-1`
* `n` is an integer.
* Either `x` is not zero or `n > 0`.
* `-104 <= xn <= 104`

## Solution

- **Language:** Python3
- **Time Complexity:** O(log N)
- **Space Complexity:** O(1)

### Approach
The solution uses the binary exponentiation (exponentiation by squaring) algorithm. If the exponent `n` is negative, we replace `x` with `1 / x` and `n` with `-n`. We then iteratively square the base `x` and halve the exponent `n`. Whenever `n` is odd, we multiply the current product into our result. This reduces the number of multiplications from O(N) to O(log N).

### Code
```py
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n
        
        result = 1.0
        current_product = x
        while n > 0:
            if n % 2 == 1:
                result *= current_product
            current_product *= current_product
            n //= 2
        return result
```
