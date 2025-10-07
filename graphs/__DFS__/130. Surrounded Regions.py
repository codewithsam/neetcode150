from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        visited = [[False for _ in range(cols)] for _ in range(rows)]

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or visited[r][c] or board[r][c] != "O":
                return
            visited[r][c] = True
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc
                dfs(nr, nc)

        for col in range(cols):
            # for cols
            if not visited[0][col] and board[0][col] == "O":
                dfs(0, col)
            if not visited[rows - 1][col] and board[rows - 1][col] == "O":
                dfs(rows - 1, col)

        for row in range(rows):
            # for rows
            if not visited[row][0] and board[row][0] == "O":
                dfs(row, 0)
            if not visited[row][cols - 1] and board[row][cols - 1] == "O":
                dfs(row, cols - 1)

        for row in range(rows):
            for col in range(cols):
                if not visited[row][col] and board[row][col] == "O":
                    board[row][col] = "X"
        return board


sol = Solution()
print(sol.solve([["O", "X", "X", "X"], ["X", "O", "O", "X"], ["O", "X", "O", "X"], ["O", "O", "X", "X"]]))
