from collections import deque
from typing import List

##################  MULTI-SOURCE BFS APPROACH #####################


class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()
        rows, cols = len(grid), len(grid[0])
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    q.append((row, col, 0))

        visited = [[False for _ in range(cols)] for _ in range(rows)]

        while q:
            row, col, d = q.popleft()
            if row < 0 or row >= rows or col < 0 or col >= cols or visited[row][col] or grid[row][col] == -1:
                continue
            visited[row][col] = True
            if grid[row][col] == 2147483647:
                grid[row][col] = d
            q.append((row + 1, col, 1 + d))
            q.append((row - 1, col, 1 + d))
            q.append((row, col + 1, 1 + d))
            q.append((row, col - 1, 1 + d))
        return grid


sol = Solution()

print(
    sol.islandsAndTreasure(
        [
            [2147483647, -1, 0, 2147483647],
            [2147483647, 2147483647, 2147483647, -1],
            [2147483647, -1, 2147483647, -1],
            [0, -1, 2147483647, 2147483647],
        ]
    )
)
