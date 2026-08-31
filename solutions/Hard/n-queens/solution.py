class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        cols = set()
        diag1 = set()  # row - col
        diag2 = set()  # row + col
        board = []
        
        def backtrack(row):
            if row == n:
                ans.append(["." * col + "Q" + "." * (n - col - 1) for col in board])
                return
            
            for col in range(n):
                if col in cols or (row - col) in diag1 or (row + col) in diag2:
                    continue
                
                cols.add(col)
                diag1.add(row - col)
                diag2.add(row + col)
                board.append(col)
                
                backtrack(row + 1)
                
                cols.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)
                board.pop()
        
        backtrack(0)
        return ans
