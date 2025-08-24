from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1]*n
        pref = 1
        for i in range(len(nums)):
            res[i] = pref
            pref *= nums[i]
        post = 1
        for i in range(n-1, -1, -1):
            res[i] *= post
            post *= nums[i]
        return res
    
sol = Solution()
print(sol.productExceptSelf([1,2,3,4]))