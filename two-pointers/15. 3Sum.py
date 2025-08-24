from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i,num in enumerate(nums):
            if i>0 and num == nums[i-1]:
                continue
            left = i+1
            right = len(nums)-1
            while left < right:
                total = num+nums[left]+nums[right]
                if total > 0:
                    right-=1
                elif total < 0:
                    left+=1
                else:
                    res.append([num, nums[left], nums[right]])
                    left+=1
                    while nums[left] == nums[left-1] and left < right:
                        left+=1
        return res

sol = Solution()
print(sol.threeSum([-1,0,1,2,-1,-4]))