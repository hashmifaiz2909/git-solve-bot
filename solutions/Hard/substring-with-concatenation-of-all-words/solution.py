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
