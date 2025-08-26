from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        while l<=r:
            if nums[l]==nums[r]: return nums[l]
            mid = int(l+(r-l)/2)
            if nums[l] > nums[r] and nums[mid] >=nums[r]:
                l = mid+1
            else:
                r = mid
    
sol = Solution()

print(sol.findMin([3,4,5,6,1,2]))
print(sol.findMin([4,5,0,1,2,3]))
