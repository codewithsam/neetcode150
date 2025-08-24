from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [[False for _ in range(9)] for _ in range(9)]
        col = [[False for _ in range(9)] for _ in range(9)]
        block = [[False for _ in range(9)] for _ in range(9)]

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                digit = int(board[r][c]) -1
                blockrow = r//3
                blockcol = c//3
                blockid = blockrow*3+blockcol
                if row[r][digit] == True or col[c][digit] == True or block[blockid][digit] == True:
                    return False
                row[r][digit] = col[c][digit] = block[blockid][digit] = True
        return True


board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
sol = Solution()
print(sol.isValidSudoku(board))