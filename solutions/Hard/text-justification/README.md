# Text Justification

**Difficulty:** Hard  
**LeetCode Link:** [Open Problem](https://leetcode.com/problems/text-justification/)

## Problem Description
Given an array of strings `words` and a width `maxWidth`, format the text such that each line has exactly `maxWidth` characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces `' '` when necessary so that each line has exactly `maxWidth` characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line does not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left-justified, and no extra space is inserted between words.

**Note:**

* A word is defined as a character sequence consisting of non-space characters only.
* Each word's length is guaranteed to be greater than `0` and not exceed `maxWidth`.
* The input array `words` contains at least one word.

**Example 1:**

```
Input: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
```

**Example 2:**

```
Input: words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16
Output:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
Explanation: Note that the last line is "shall be    " instead of "shall     be", because the last line must be left-justified instead of fully-justified.
Note that the second line is also left-justified because it contains only one word.
```

**Example 3:**

```
Input: words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], maxWidth = 20
Output:
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]
```

**Constraints:**

* `1 <= words.length <= 300`
* `1 <= words[i].length <= 20`
* `words[i]` consists of only English letters and symbols.
* `1 <= maxWidth <= 100`
* `words[i].length <= maxWidth`

## Solution

- **Language:** Python3
- **Time Complexity:** O(N)
- **Space Complexity:** O(M)

### Approach
We process words greedily to fit as many words as possible into the current line. We track `cur_words` and their cumulative length `cur_len`. When adding another word exceeds `maxWidth`, we format the current line. For fully justified lines with multiple words, we calculate total spaces, base spaces per gap, and distribute extra spaces starting from the leftmost gaps. Lines with a single word or the final line are formatted left-justified by joining words with a single space and appending padding spaces at the end.

### Code
```py
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        cur_words = []
        cur_len = 0
        
        for word in words:
            if cur_len + len(word) + len(cur_words) > maxWidth:
                if len(cur_words) == 1:
                    res.append(cur_words[0] + ' ' * (maxWidth - cur_len))
                else:
                    total_spaces = maxWidth - cur_len
                    gaps = len(cur_words) - 1
                    space_per_gap = total_spaces // gaps
                    extra_spaces = total_spaces % gaps
                    
                    line = []
                    for i in range(gaps):
                        line.append(cur_words[i])
                        line.append(' ' * (space_per_gap + (1 if i < extra_spaces else 0)))
                    line.append(cur_words[-1])
                    res.append(''.join(line))
                
                cur_words = [word]
                cur_len = len(word)
            else:
                cur_words.append(word)
                cur_len += len(word)
        
        last_line = ' '.join(cur_words)
        last_line += ' ' * (maxWidth - len(last_line))
        res.append(last_line)
        
        return res
```
