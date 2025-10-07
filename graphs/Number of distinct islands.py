from collections import deque

######## https://takeuforward.org/plus/dsa/problems/number-of-distinct-islands


class Solution:
    def countDistinctIslands(self, grid):
        rows, cols = len(grid), len(grid[0])
        visited = [[False for _ in range(cols)] for _ in range(rows)]
        res = set()
        total = 0

        def dfs(r, c, base):
            nonlocal cells
            if r < 0 or r >= rows or c < 0 or c >= cols or visited[r][c] or grid[r][c] != 1:
                return
            visited[r][c] = True
            cells.append((r - base[0], c - base[1]))
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                dfs(r + dr, c + dc, base)

        for row in range(rows):
            for col in range(cols):
                if not visited[row][col] and grid[row][col] == 1:
                    cells = []
                    dfs(row, col, (row, col))
                    t = tuple(cells)
                    if t not in res:
                        total += 1
                        res.add(t)
        return total


sol = Solution()

print(sol.countDistinctIslands([[1, 1, 0, 1, 1], [1, 0, 0, 0, 0], [0, 0, 0, 0, 1], [1, 1, 0, 1, 1]]))  # 3
print(sol.countDistinctIslands([[1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 0, 1, 1], [0, 0, 0, 1, 1]]))  # 1

# Case 1: Two identical 2x2 islands → 1 distinct
print(sol.countDistinctIslands([[1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 0, 1, 1], [0, 0, 0, 1, 1]]))  # Expected: 1

# Case 2: L-shaped and line island → 2 distinct
print(sol.countDistinctIslands([[1, 1, 0, 1], [1, 0, 0, 0], [0, 0, 0, 1]]))  # Expected: 2

# Case 3: All single-cell islands → 1 distinct
print(sol.countDistinctIslands([[1, 0, 1], [0, 1, 0], [1, 0, 1]]))  # Expected: 1

# Case 4: Big connected island → 1 distinct
print(sol.countDistinctIslands([[1, 1, 1], [1, 1, 1], [1, 1, 1]]))  # Expected: 1

# Case 5: No land → 0
print(sol.countDistinctIslands([[0, 0, 0], [0, 0, 0], [0, 0, 0]]))  # Expected: 0

# Case 6: Distinct shapes (L, line, square) → 3 distinct
print(sol.countDistinctIslands([[1, 0, 1, 1], [1, 0, 0, 1], [0, 0, 0, 0], [1, 1, 0, 0]]))  # Expected: 3
