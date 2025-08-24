from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row,col = len(matrix), len(matrix[0])
        l,r = 0, row*col-1
        while l<=r:
            mid = int(l+(r-l)/2)
            crow = int(mid/row)
            ccol = mid%col
            if target > matrix[crow][ccol]:
                l = mid+1
            elif target < matrix[crow][ccol]:
                r = mid-1
            else:
                return True
        
        return False

sol = Solution()
print(sol.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13))
print(sol.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))