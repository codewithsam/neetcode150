from typing import List


class Solution:
    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        def _isValid(move, row, col):
            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid) or grid[row][col] != move:
                return False
            if move == (len(grid) * len(grid)) - 1:
                return True
            valid = (
                _isValid(move + 1, row - 2, col - 1)
                or _isValid(move + 1, row - 2, col + 1)
                or _isValid(move + 1, row + 2, col - 1)
                or _isValid(move + 1, row + 2, col + 1)
                or _isValid(move + 1, row - 1, col - 2)
                or _isValid(move + 1, row + 1, col - 2)
                or _isValid(move + 1, row - 1, col + 2)
                or _isValid(move + 1, row + 1, col + 2)
            )
            return valid

        return _isValid(0, 0, 0)


sol = Solution()
print(
    sol.checkValidGrid(
        [[0, 11, 16, 5, 20], [17, 4, 19, 10, 15], [12, 1, 8, 21, 6], [3, 18, 23, 14, 9], [24, 13, 2, 7, 22]]
    )
)  # true
print(sol.checkValidGrid([[0, 3, 6], [5, 8, 1], [2, 7, 4]]))  # false
