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
