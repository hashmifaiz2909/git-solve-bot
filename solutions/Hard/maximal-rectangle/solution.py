class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        
        cols = len(matrix[0])
        heights = [0] * cols
        max_area = 0
        
        for row in matrix:
            for c in range(cols):
                if row[c] == '1':
                    heights[c] += 1
                else:
                    heights[c] = 0
            
            # Calculate the maximum rectangle in the histogram for the current row
            stack = []
            extended_heights = heights + [0]
            for i, h in enumerate(extended_heights):
                while stack and extended_heights[stack[-1]] > h:
                    height_idx = stack.pop()
                    height = extended_heights[height_idx]
                    width = i if not stack else i - stack[-1] - 1
                    max_area = max(max_area, height * width)
                stack.append(i)
                
        return max_area
