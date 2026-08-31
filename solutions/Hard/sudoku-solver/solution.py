class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = [0] * 9
        cols = [0] * 9
        boxes = [0] * 9
        empty = []

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    empty.append((r, c))
                else:
                    digit = int(board[r][c]) - 1
                    mask = 1 << digit
                    rows[r] |= mask
                    cols[c] |= mask
                    boxes[(r // 3) * 3 + c // 3] |= mask

        def backtrack(empty_idx: int) -> bool:
            if empty_idx == len(empty):
                return True

            best_i = empty_idx
            min_choices = 10
            best_mask = 0

            for i in range(empty_idx, len(empty)):
                r, c = empty[i]
                b = (r // 3) * 3 + c // 3
                mask = 0x1FF & ~(rows[r] | cols[c] | boxes[b])
                choices = bin(mask).count('1')
                if choices < min_choices:
                    min_choices = choices
                    best_i = i
                    best_mask = mask
                if min_choices == 0:
                    break

            if min_choices == 0:
                return False

            empty[empty_idx], empty[best_i] = empty[best_i], empty[empty_idx]
            r, c = empty[empty_idx]
            b = (r // 3) * 3 + c // 3

            while best_mask:
                lsb = best_mask & -best_mask
                digit = lsb.bit_length() - 1

                board[r][c] = str(digit + 1)
                rows[r] |= lsb
                cols[c] |= lsb
                boxes[b] |= lsb

                if backtrack(empty_idx + 1):
                    return True

                rows[r] ^= lsb
                cols[c] ^= lsb
                boxes[b] ^= lsb
                board[r][c] = '.'
                best_mask &= best_mask - 1

            empty[empty_idx], empty[best_i] = empty[best_i], empty[empty_idx]
            return False

        backtrack(0)
