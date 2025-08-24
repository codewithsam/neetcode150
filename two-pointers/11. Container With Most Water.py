from typing import List


class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r = 0, len(heights)-1
        height = 0
        while l < r:
            m = min(heights[l],heights[r])
            area = m* (r-l)
            height = max(area, height)
            if heights[l] < heights[r]:
                l+=1
            else:
                r-=1
        return height
    

sol = Solution()
print(sol.maxArea([1,7,2,5,4,7,3,6]))