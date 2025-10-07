from collections import deque
from typing import List


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] == 1 or grid[n - 1][n - 1]:
            return -1
        distance = [[float("inf") for _ in grid[0]] for _ in grid]
        q = deque()
        q.append((1, (0, 0)))
        distance[0][0] = 1

        while q:
            dist, (row, col) = q.popleft()
            if row == n - 1 and col == n - 1:
                return dist
            if dist > distance[row][col]:
                continue
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (-1, 1), (1, -1)]

            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if nr < 0 or nr >= n or nc < 0 or nc >= n or grid[nr][nc] == 1:
                    continue
                nextdist = distance[row][col] + 1
                if nextdist < distance[nr][nc]:
                    distance[nr][nc] = nextdist
                    q.append((nextdist, (nr, nc)))
        print(distance)

        return -1


sol = Solution()

print(sol.shortestPathBinaryMatrix([[0, 0, 0], [1, 1, 0], [1, 1, 0]]))
print(sol.shortestPathBinaryMatrix([[1, 0, 0], [1, 1, 0], [1, 1, 0]]))
print(
    sol.shortestPathBinaryMatrix(
        [
            [0, 1, 1, 0, 0, 0],
            [0, 1, 0, 1, 1, 0],
            [0, 1, 1, 0, 1, 0],
            [0, 0, 0, 1, 1, 0],
            [1, 1, 1, 1, 1, 0],
            [1, 1, 1, 1, 1, 0],
        ]
    )
)
