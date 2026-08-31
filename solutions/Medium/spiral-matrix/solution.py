class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        
        result = []
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1
        
        while top <= bottom and left <= right:
            # Traverse Right
            for c in range(left, right + 1):
                result.append(matrix[top][c])
            top += 1
            
            # Traverse Down
            for r in range(top, bottom + 1):
                result.append(matrix[r][right])
            right -= 1
            
            # Traverse Left
            if top <= bottom:
                for c in range(right, left - 1, -1):
                    result.append(matrix[bottom][c])
                bottom -= 1
            
            # Traverse Up
            if left <= right:
                for r in range(bottom, top - 1, -1):
                    result.append(matrix[r][left])
                left += 1
                
        return result
