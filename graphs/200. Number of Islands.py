from collections import deque
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        output = 0

        def _dfs(row, col):
            if row >= rows or col >= cols or row < 0 or col < 0 or grid[row][col] == "0":
                return

            grid[row][col] = "0"
            _dfs(row + 1, col)
            _dfs(row - 1, col)
            _dfs(row, col + 1)
            _dfs(row, col - 1)

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    output += 1
                    _dfs(row, col)
        return output


sol = Solution()
print(
    sol.numIslands(
        [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]
    )
)
print(
    sol.numIslands(
        [["1", "1", "0", "0", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "1", "0", "0"], ["0", "0", "0", "1", "1"]]
    )
)
