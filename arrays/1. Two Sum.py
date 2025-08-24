from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for idx, num in enumerate(nums):
            remainder = target-num
            if remainder in seen:
                return [seen[remainder], idx]
            else:
                seen[num] = idx
        return []
    

sol = Solution()
nums, target = [3,2,4], 6
print(sol.twoSum(nums, target))