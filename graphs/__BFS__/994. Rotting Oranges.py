from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    q.append((row, col))
        time = 0

        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = 2
                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nr, nc = r + dr, c + dc
                    if nr < 0 or nr >= rows or nc < 0 or nc >= cols or grid[nr][nc] != 1:
                        continue
                    grid[nr][nc] = 2
                    q.append((nr, nc))
            if q:
                time += 1

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    return -1
        return time


print(Solution().orangesRotting([[1, 1, 0], [0, 1, 1], [0, 1, 2]]))
print(Solution().orangesRotting([[1, 0, 1], [0, 2, 0], [1, 0, 1]]))
print(Solution().orangesRotting([[0]]))
