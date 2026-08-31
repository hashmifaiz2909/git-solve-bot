# Valid Number

**Difficulty:** Hard  
**LeetCode Link:** [Open Problem](https://leetcode.com/problems/valid-number/)

## Problem Description
Given a string `s`, return whether `s` is a **valid number**.  
  
For example, all the following are valid numbers: `"2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"`, while the following are not valid numbers: `"abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"`.

Formally, a **valid number** is defined using one of the following definitions:

1. An **integer number** followed by an **optional exponent**.
2. A **decimal number** followed by an **optional exponent**.

An **integer number** is defined with an **optional sign** `'-'` or `'+'` followed by **digits**.

A **decimal number** is defined with an **optional sign** `'-'` or `'+'` followed by one of the following definitions:

1. **Digits** followed by a **dot** `'.'`.
2. **Digits** followed by a **dot** `'.'` followed by **digits**.
3. A **dot** `'.'` followed by **digits**.

An **exponent** is defined with an **exponent notation** `'e'` or `'E'` followed by an **integer number**.

The **digits** are defined as one or more digits.

**Example 1:**

**Input:** s = "0"

**Output:** true

**Example 2:**

**Input:** s = "e"

**Output:** false

**Example 3:**

**Input:** s = "."

**Output:** false

**Constraints:**

* `1 <= s.length <= 20`
* `s` consists of only English letters (both uppercase and lowercase), digits (`0-9`), plus `'+'`, minus `'-'`, or dot `'.'`.

## Solution

- **Language:** Python3
- **Time Complexity:** O(N), where N is the length of the string s, as we iterate through the string once.
- **Space Complexity:** O(1), since we only use a constant amount of extra memory for state flags.

### Approach
We iterate through the characters of the string while maintaining state flags: `seen_digit`, `seen_dot`, and `seen_exponent`.
- A digit sets `seen_digit` to `True`.
- A sign (`+` or `-`) is only valid at index 0 or immediately following an exponent character (`e` or `E`).
- A dot (`.`) is only valid if we have not encountered a dot or an exponent yet.
- An exponent character (`e` or `E`) is only valid if we have not seen an exponent yet and have already seen at least one digit before it. Encountering an exponent resets `seen_digit` to `False` to mandate at least one digit in the exponent part.
- Any other character makes the string invalid.

At the end of the loop, the number is valid if `seen_digit` is `True`.

### Code
```py
class Solution:
    def isNumber(self, s: str) -> bool:
        seen_digit = False
        seen_dot = False
        seen_exponent = False
        
        for i, c in enumerate(s):
            if c.isdigit():
                seen_digit = True
            elif c in ['+', '-']:
                if i > 0 and s[i - 1] not in ['e', 'E']:
                    return False
            elif c == '.':
                if seen_dot or seen_exponent:
                    return False
                seen_dot = True
            elif c in ['e', 'E']:
                if seen_exponent or not seen_digit:
                    return False
                seen_exponent = True
                seen_digit = False
            else:
                return False
                
        return seen_digit
```
