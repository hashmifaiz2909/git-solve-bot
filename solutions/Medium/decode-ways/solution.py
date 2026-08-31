class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0
        
        n = len(s)
        prev2 = 1
        prev1 = 1
        
        for i in range(2, n + 1):
            current = 0
            # Single digit decode
            if s[i-1] != '0':
                current += prev1
            # Two digit decode
            two_digit = int(s[i-2:i])
            if 10 <= two_digit <= 26:
                current += prev2
            
            prev2 = prev1
            prev1 = current
            
        return prev1
