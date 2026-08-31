# Substring with Concatenation of All Words

**Difficulty:** Hard  
**LeetCode Link:** [Open Problem](https://leetcode.com/problems/substring-with-concatenation-of-all-words/)

## Problem Description
You are given a string `s` and an array of strings `words`. All the strings of `words` are of **the same length**.

A **concatenated string** is a string that exactly contains all the strings of any permutation of `words` concatenated.

* For example, if `words = ["ab","cd","ef"]`, then `"abcdef"`, `"abefcd"`, `"cdabef"`, `"cdefab"`, `"efabcd"`, and `"efcdab"` are all concatenated strings. `"acdbef"` is not a concatenated string because it is not the concatenation of any permutation of `words`.

Return an array of *the starting indices* of all the concatenated substrings in `s`. You can return the answer in **any order**.

**Example 1:**

**Input:** s = "barfoothefoobarman", words = ["foo","bar"]

**Output:** [0,9]

**Explanation:**

The substring starting at 0 is `"barfoo"`. It is the concatenation of `["bar","foo"]` which is a permutation of `words`.  
The substring starting at 9 is `"foobar"`. It is the concatenation of `["foo","bar"]` which is a permutation of `words`.

**Example 2:**

**Input:** s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]

**Output:** []

**Explanation:**

There is no concatenated substring.

**Example 3:**

**Input:** s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]

**Output:** [6,9,12]

**Explanation:**

The substring starting at 6 is `"foobarthe"`. It is the concatenation of `["foo","bar","the"]`.  
The substring starting at 9 is `"barthefoo"`. It is the concatenation of `["bar","the","foo"]`.  
The substring starting at 12 is `"thefoobar"`. It is the concatenation of `["the","foo","bar"]`.

**Constraints:**

* `1 <= s.length <= 104`
* `1 <= words.length <= 5000`
* `1 <= words[i].length <= 30`
* `s` and `words[i]` consist of lowercase English letters.

## Solution

- **Language:** Python3
- **Time Complexity:** O(N * L) where N is the length of the string `s` and L is the length of each word in `words`. The outer loop runs L times, and the inner loop processes the string in steps of L, performing constant-time hash map operations of string length L.
- **Space Complexity:** O(M * L) where M is the number of words in `words` and L is the length of each word. This space is used to store the word frequencies in the hash maps.

### Approach
The problem can be solved efficiently using a sliding window approach. Since all words in `words` have the same length (`word_len`), we can partition the starting indices of our search into `word_len` groups. For each group starting at index `i` (where `0 <= i < word_len`), we slide a window of size `total_len` by steps of `word_len`. We maintain a frequency map of the words in the current window. If we encounter a word that is not in `words`, we reset the window. If a word's frequency exceeds its allowed count in `words`, we shrink the window from the left until the frequency is valid. When the window contains exactly the required number of words, we record the starting index.

### Code
```py
from collections import Counter
from typing import List

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        
        word_len = len(words[0])
        num_words = len(words)
        total_len = word_len * num_words
        
        if len(s) < total_len:
            return []
        
        word_counts = Counter(words)
        ans = []
        
        for i in range(word_len):
            left = i
            curr_count = {}
            count = 0
            
            for right in range(i, len(s) - word_len + 1, word_len):
                word = s[right : right + word_len]
                if word in word_counts:
                    curr_count[word] = curr_count.get(word, 0) + 1
                    count += 1
                    
                    while curr_count[word] > word_counts[word]:
                        left_word = s[left : left + word_len]
                        curr_count[left_word] -= 1
                        count -= 1
                        left += word_len
                        
                    if count == num_words:
                        ans.append(left)
                else:
                    curr_count.clear()
                    count = 0
                    left = right + word_len
                    
        return ans
```
