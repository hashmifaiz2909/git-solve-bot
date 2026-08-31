class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Constants for 32-bit signed integer limits
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        # Handle overflow case
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX
        
        # Determine the sign of the result
        negative = (dividend < 0) ^ (divisor < 0)
        
        # Work with absolute values
        a, b = abs(dividend), abs(divisor)
        
        quotient = 0
        # Iterate from the largest possible power of 2 down to 0
        for i in range(31, -1, -1):
            if a >= (b << i):
                a -= (b << i)
                quotient += (1 << i)
                
        if negative:
            quotient = -quotient
            
        # Clamp the result within the 32-bit signed integer range
        return max(INT_MIN, min(INT_MAX, quotient))
