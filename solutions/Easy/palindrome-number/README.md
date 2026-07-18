# Palindrome Number

**Difficulty:** Easy  
**LeetCode Link:** [Open Problem](https://leetcode.com/problems/palindrome-number/)

## Problem Description
Given an integer `x`, return `true` *if* `x` *is a* ***palindrome****, and* `false` *otherwise*.

**Example 1:**

```
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
```

**Example 2:**

```
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
```

**Example 3:**

```
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
```

**Constraints:**

* `-231 <= x <= 231 - 1`

**Follow up:** Could you solve it without converting the integer to a string?

## Solution

- **Language:** Python3
- **Time Complexity:** O(log10(N))
- **Space Complexity:** O(1)

### Approach
The algorithm reverses the second half of the integer and compares it with the first half. If they are equal, the number is a palindrome. We can detect when we have reached the middle of the number when the original number becomes less than or equal to the reversed number. This approach avoids integer overflow issues and does not require converting the integer to a string.

### Code
```py
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Special cases:
        # As discussed above, when x < 0, x is not a palindrome.
        # Also if the last digit of the number is 0, to be a palindrome,
        # the first digit of the number also needs to be 0.
        # Only 0 satisfy this property.
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        revertedNumber = 0
        while x > revertedNumber:
            revertedNumber = revertedNumber * 10 + x % 10
            x //= 10

        # When the length is an odd number, we can get rid of the middle digit by revertedNumber // 10
        # For example when x = 12321, at the end of the while loop we get x = 12, revertedNumber = 123,
        # since the middle digit doesn't matter in palindrome (it will always equal to itself),
        # we can simply get rid of it.
        return x == revertedNumber or x == revertedNumber // 10
```
