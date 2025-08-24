from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lower = prices[0]
        maxProfit = 0
        for num in prices:
            if  num < lower:
                lower = num
            else:
                maxProfit = max(maxProfit, num - lower)
        return maxProfit
    
sol = Solution()
print(sol.maxProfit([7,1,5,3,6,4]))