from collections import deque
from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        q = deque()
        visited = [[False for _ in range(cols)] for _ in range(rows)]
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == "O":
                    collision = False
                    regions = set()
                    q.append((row, col))
                    regions.add((row, col))
                    visited[row][col] = True
                    if row == 0 or row == rows - 1 or col == 0 or col == cols - 1:
                        collision = True
                    while q:
                        r, c = q.popleft()
                        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                            nr, nc = r + dr, c + dc
                            if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc]:
                                visited[nr][nc] = True
                                if board[nr][nc] == "O":
                                    q.append((nr, nc))
                                    regions.add((nr, nc))
                                    if nr == 0 or nr == rows - 1 or nc == 0 or nc == cols - 1:
                                        collision = True

                    if not collision:
                        for r, c in regions:
                            board[r][c] = "X"
        return board


sol = Solution()

print(sol.solve([["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]]))


######################### MORE OPTIMIZED SOLUTION OF BFS WHERE WE CHECK BORDERS ############################


class OBFS:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        visited = [[False for _ in range(cols)] for _ in range(rows)]

        def bfs(r, c):
            q = deque()
            q.append((r, c))
            visited[r][c] = True
            while q:
                r, c = q.popleft()
                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc] and board[nr][nc] == "O":
                        visited[nr][nc] = True
                        q.append((nr, nc))

        for r in range(rows):
            for c in [0, cols - 1]:
                if board[r][c] == "O" and not visited[r][c]:
                    bfs(r, c)

        for c in range(cols):
            for r in [0, rows - 1]:
                if board[r][c] == "O" and not visited[r][c]:
                    bfs(r, c)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and not visited[r][c]:
                    board[r][c] = "X"

        return board


obfs = OBFS()

print(obfs.solve([["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]]))
