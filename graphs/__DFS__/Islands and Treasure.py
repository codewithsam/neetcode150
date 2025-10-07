from typing import List


############################                          #################################
#
#                   DFS IS LESS EFFICIENT SINCE ON EVERY GATE (0) WE RECOMPUTE ALREADY
#                        COMPUTED CELLS TO UPDATE IF THE NEW DISTANCE IS SMALLER
#
#                           GO WITH BFS MULTI-SOURCE FLOOD FILL APPROACH
#
############################                          #################################


class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        INF = 2147483647

        def dfs(r, c, dist):
            # out of bounds or wall
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] < dist:
                return
            grid[r][c] = dist
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                dfs(r + dr, c + dc, dist + 1)

        # Start DFS from every gate
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    dfs(r, c, 0)

        return grid
