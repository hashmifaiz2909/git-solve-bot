# Length of Last Word

**Difficulty:** Easy  
**LeetCode Link:** [Open Problem](https://leetcode.com/problems/length-of-last-word/)

## Problem Description
Given a string `s` consisting of words and spaces, return *the length of the **last** word in the string.*

A **word** is a maximal substring consisting of non-space characters only.

**Example 1:**

```
Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.
```

**Example 2:**

```
Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.
```

**Example 3:**

```
Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.
```

**Constraints:**

* `1 <= s.length <= 104`
* `s` consists of only English letters and spaces `' '`.
* There will be at least one word in `s`.

## Solution

- **Language:** Python3
- **Time Complexity:** O(N)
- **Space Complexity:** O(1)

### Approach
The algorithm starts from the end of the string and skips any trailing spaces. Once a non-space character is encountered, it counts the consecutive non-space characters until a space or the beginning of the string is reached. This count represents the length of the last word.

### Code
```py
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        i = len(s) - 1
        
        # Skip trailing spaces
        while i >= 0 and s[i] == ' ':
            i -= 1
            
        # Count characters of the last word
        while i >= 0 and s[i] != ' ':
            length += 1
            i -= 1
            
        return length
```
