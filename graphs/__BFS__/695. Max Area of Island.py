from collections import deque
from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        area = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    q = deque()
                    grid[row][col] = 0
                    q.append((row, col))
                    count = 0
                    while q:
                        r, c = q.popleft()
                        count += 1
                        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                            nr, nc = r + dr, c + dc
                            if nr < 0 or nr >= rows or nc < 0 or nc >= cols or grid[nr][nc] != 1:
                                continue
                            else:
                                grid[nr][nc] = 0
                                q.append((nr, nc))
                    area = max(area, count)
        return area


# print(Solution().maxAreaOfIsland([[0, 1, 1, 0, 1], [1, 0, 1, 0, 1], [0, 1, 1, 0, 1], [0, 1, 0, 0, 1]]))#
print(Solution().maxAreaOfIsland([[1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 0, 1, 1], [0, 0, 0, 1, 1]]))
