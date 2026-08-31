class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        R, C = len(board), len(board[0])
        
        # Pruning 1: Check if the grid has enough of each character required by word
        board_counts = Counter(char for row in board for char in row)
        word_counts = Counter(word)
        for char, count in word_counts.items():
            if board_counts[char] < count:
                return False
        
        # Pruning 2: Start search from the end with fewer matching characters in board
        if board_counts[word[0]] > board_counts[word[-1]]:
            word = word[::-1]
            
        def dfs(r: int, c: int, idx: int) -> bool:
            if idx == len(word):
                return True
            if r < 0 or r >= R or c < 0 or c >= C or board[r][c] != word[idx]:
                return False
            
            temp = board[r][c]
            board[r][c] = '#'
            
            res = (dfs(r + 1, c, idx + 1) or
                   dfs(r - 1, c, idx + 1) or
                   dfs(r, c + 1, idx + 1) or
                   dfs(r, c - 1, idx + 1))
                   
            board[r][c] = temp
            return res
        
        for r in range(R):
            for c in range(C):
                if board[r][c] == word[0] and dfs(r, c, 0):
                    return True
                    
        return False
