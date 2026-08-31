class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        
        # Ensure s2 is the shorter string to optimize space complexity to O(min(len(s1), len(s2)))
        if len(s1) < len(s2):
            s1, s2 = s2, s1
            
        n, m = len(s1), len(s2)
        dp = [False] * (m + 1)
        
        # Base case: empty s1 and empty s2
        dp[0] = True
        
        # Initialize DP for i = 0 (only using characters from s2)
        for j in range(1, m + 1):
            dp[j] = dp[j - 1] and s2[j - 1] == s3[j - 1]
            
        # Fill the DP table row by row
        for i in range(1, n + 1):
            dp[0] = dp[0] and s1[i - 1] == s3[i - 1]
            for j in range(1, m + 1):
                dp[j] = (dp[j] and s1[i - 1] == s3[i + j - 1]) or (dp[j - 1] and s2[j - 1] == s3[i + j - 1])
                
        return dp[m]
