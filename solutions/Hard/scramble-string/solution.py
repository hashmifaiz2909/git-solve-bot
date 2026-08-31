class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        memo = {}
        
        def dfs(i1, i2, length):
            state = (i1, i2, length)
            if state in memo:
                return memo[state]
            
            sub1 = s1[i1:i1+length]
            sub2 = s2[i2:i2+length]
            
            if sub1 == sub2:
                memo[state] = True
                return True
            
            # Pruning: If the sorted characters of the two substrings do not match,
            # they cannot be scrambled versions of each other.
            if sorted(sub1) != sorted(sub2):
                memo[state] = False
                return False
            
            for i in range(1, length):
                # Case 1: No swap at the current split point
                if dfs(i1, i2, i) and dfs(i1 + i, i2 + i, length - i):
                    memo[state] = True
                    return True
                # Case 2: Swap at the current split point
                if dfs(i1, i2 + length - i, i) and dfs(i1 + i, i2, length - i):
                    memo[state] = True
                    return True
            
            memo[state] = False
            return False
        
        return dfs(0, 0, len(s1))
