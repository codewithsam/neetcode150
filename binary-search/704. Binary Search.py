from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums)-1
        while l<=r:
            mid = int(l+(r-l)/2)
            if target>nums[mid]:
                l=mid+1
            elif target<nums[mid]:
                r = mid-1
            else:
                return mid
        return -1


sol = Solution()
# print(sol.search([-1,0,3,5,9,12], 9))
# print(sol.search([-1,0,3,5,9,12], 2))
print(sol.search([-1,0,2,4,6,8], 4))
