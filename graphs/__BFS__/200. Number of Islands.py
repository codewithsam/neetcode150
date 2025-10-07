from collections import deque
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        count = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    grid[row][col] = "2"
                    count += 1
                    q.append((row, col))
                    while q:
                        r, c = q.popleft()
                        if grid[r][c] == "1":
                            grid[r][c] = "2"

                        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                            nr, nc = r + dr, c + dc
                            if nc < 0 or nc >= cols or nr < 0 or nr >= rows or grid[nr][nc] != "1":
                                continue
                            q.append((nr, nc))
        return count


sol = Solution()
print(
    sol.numIslands(
        [["0", "1", "1", "1", "0"], ["0", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]
    )
)

print(
    sol.numIslands(
        [["1", "1", "0", "0", "1"], ["1", "1", "0", "0", "1"], ["0", "0", "1", "0", "0"], ["0", "0", "0", "1", "1"]]
    )
)
