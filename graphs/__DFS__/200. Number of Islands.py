from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        count = 0

        def _dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] != "1":
                return

            grid[r][c] = "2"

            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                _dfs(dr + r, dc + c)

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    count += 1
                    _dfs(row, col)
        return count
