from collections import deque
from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # pacific is row 0 and col 0-5 or col 0 and row 0-5
        # atlantic is row n-1 and col 0-5 or col n-1 and row 0-5

        def _bfs(setobj, q):
            dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            while q:
                r, c = q.popleft()
                setobj.add((r, c))
                for dr, dc in dir:
                    nr, nc = r + dr, c + dc
                    if (
                        nr >= 0
                        and nr < rows
                        and nc >= 0
                        and nc < cols
                        and heights[r][c] <= heights[nr][nc]
                        and (nr, nc) not in setobj
                    ):
                        q.append((nr, nc))

        rows, cols = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()
        # ---- Pacific initialization ----
        q = deque()
        for c in range(cols):  # top row
            q.append((0, c))
        for r in range(rows):  # left column
            q.append((r, 0))

        _bfs(pacific, q)

        q = deque()

        # ---- Atlantic initialization ----
        for c in range(cols):  # bottom row
            q.append((rows - 1, c))
        for r in range(rows):  # right column
            q.append((r, cols - 1))

        _bfs(atlantic, q)

        return [list(cell) for cell in pacific & atlantic]


sol = Solution()

print(sol.pacificAtlantic([[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]))
