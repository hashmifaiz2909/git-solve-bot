class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        
        # KMP Algorithm
        # Step 1: Build the LPS (Longest Prefix Suffix) array
        lps = [0] * len(needle)
        prevLPS, i = 0, 1
        while i < len(needle):
            if needle[i] == needle[prevLPS]:
                lps[i] = prevLPS + 1
                prevLPS += 1
                i += 1
            else:
                if prevLPS == 0:
                    lps[i] = 0
                    i += 1
                else:
                    prevLPS = lps[prevLPS - 1]
        
        # Step 2: Search the needle in the haystack
        i = 0  # index for haystack
        j = 0  # index for needle
        while i < len(haystack):
            if haystack[i] == needle[j]:
                i += 1
                j += 1
            else:
                if j == 0:
                    i += 1
                else:
                    j = lps[j - 1]
            
            if j == len(needle):
                return i - len(needle)
        
        return -1
