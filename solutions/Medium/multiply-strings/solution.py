class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        
        m, n = len(num1), len(num2)
        res = [0] * (m + n)
        
        num1_rev = num1[::-1]
        num2_rev = num2[::-1]
        
        for i in range(m):
            for j in range(n):
                res[i + j] += int(num1_rev[i]) * int(num2_rev[j])
                
        for k in range(len(res) - 1):
            res[k + 1] += res[k] // 10
            res[k] %= 10
            
        while len(res) > 1 and res[-1] == 0:
            res.pop()
            
        return "".join(str(d) for d in res[::-1])
