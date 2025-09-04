from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["." for _ in range(0, n)] for _ in range(0, n)]
        cols = set()
        posD = set()
        negD = set()
        res = []

        def _queens(row):
            if row == n:
                copyboard = ["".join(r) for r in board]
                res.append(copyboard)
                return

            for col in range(n):
                if col in cols or (row + col) in posD or (row - col) in negD:
                    continue

                board[row][col] = "Q"
                cols.add(col)
                posD.add(row + col)
                negD.add(row - col)

                _queens(row + 1)

                cols.remove(col)
                posD.remove(row + col)
                negD.remove(row - col)
                board[row][col] = "."

        _queens(0)
        return res


sol = Solution()

print(sol.solveNQueens(4))
