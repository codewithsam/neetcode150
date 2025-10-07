from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = 9
        row = {i: set() for i in range(n)}
        col = {i: set() for i in range(n)}
        block = {(br, bc): set() for bc in range(n) for br in range(n)}

        for r in range(n):
            for c in range(n):
                if board[r][c] == ".":
                    continue
                digit = int(board[r][c])
                br = r // 3
                bc = c // 3
                if digit in row[r] or digit in col[c] or digit in block[(br, bc)]:
                    return False
                row[r].add(digit)
                col[c].add(digit)
                block[(br, bc)].add(digit)
        return True


board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]
sol = Solution()
print(sol.isValidSudoku(board))
