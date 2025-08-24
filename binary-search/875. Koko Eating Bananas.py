from typing import List
import math


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1, max(piles)
        while l<=r:
            k = int(l+(r-l)/2)
            totaltime = 0
            for pile in piles:
                totaltime+= math.ceil(pile/k)
            if totaltime <= h:
                res = k
                r = k-1
            else: l=k+1
        return res

sol = Solution()

print(sol.minEatingSpeed([3,6,7,11],8)) # 4
print(sol.minEatingSpeed([30,11,23,4,20],5)) # 30
print(sol.minEatingSpeed([30,11,23,4,20],6)) # 23
