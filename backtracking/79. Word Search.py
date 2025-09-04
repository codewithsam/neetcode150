from typing import Counter, List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        word = list(word)
        rows, cols = len(board), len(board[0])
        visited = [[False for _ in range(cols)] for _ in range(rows)]

        def _exist(r, c, i):
            if i == len(word):
                return True
            if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != word[i]:
                return

            visited[r][c] = True

            found = (
                _exist(row - 1, col, i + 1)
                or _exist(row + 1, col, i + 1)
                or _exist(row, col - 1, i + 1)
                or _exist(row, col + 1, i + 1)
            )

            visited[row][col] = False
            return found

        for row in range(rows):
            for col in range(cols):
                if _exist(row, col, 0):
                    return True

        return False


sol = Solution()
print(sol.exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCCED"))
print(sol.exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "SEE"))
print(sol.exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCB"))
