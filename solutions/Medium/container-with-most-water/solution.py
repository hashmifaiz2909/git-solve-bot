class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0
        
        while left < right:
            h_left = height[left]
            h_right = height[right]
            current_area = min(h_left, h_right) * (right - left)
            if current_area > max_area:
                max_area = current_area
            
            if h_left < h_right:
                left += 1
            else:
                right -= 1
                
        return max_area
