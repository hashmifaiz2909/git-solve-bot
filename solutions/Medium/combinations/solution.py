from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        def backtrack(start: int, path: List[int]):
            if len(path) == k:
                result.append(list(path))
                return
            
            # Pruning: only loop if there are enough remaining elements to form a combination of size k
            for i in range(start, n - (k - len(path)) + 2):
                path.append(i)
                backtrack(i + 1, path)
                path.pop()
                
        backtrack(1, [])
        return result
