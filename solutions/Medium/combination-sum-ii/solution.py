class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        results = []
        
        def backtrack(start: int, remaining: int, path: List[int]):
            if remaining == 0:
                results.append(list(path))
                return
            
            for i in range(start, len(candidates)):
                if candidates[i] > remaining:
                    break
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                
                path.append(candidates[i])
                backtrack(i + 1, remaining - candidates[i], path)
                path.pop()
                
        backtrack(0, target, [])
        return results
