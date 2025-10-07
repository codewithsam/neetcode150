from collections import deque
from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
        visited = [[False for _ in range(cols)] for _ in range(rows)]
        res = [[-1 for _ in range(cols)] for _ in range(rows)]
        q = deque()
        for row in range(rows):
            for col in range(cols):
                if mat[row][col] == 0:
                    q.append((row, col, 0))
                    visited[row][col] = True
        while q:
            r, c, d = q.popleft()
            res[r][c] = d
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc] and mat[nr][nc] != 0:
                    q.append((nr, nc, d + 1))
                    visited[nr][nc] = True

        return res


sol = Solution()

print(sol.updateMatrix([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))
print(sol.updateMatrix([[0, 0, 0], [0, 1, 0], [1, 1, 1]]))
