from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        count = 0
        for num in seen:
            if num-1 not in seen:
                curr = 1
                while num+curr in seen:
                    curr +=1
                count = max(curr, count)
        return count

sol = Solution()
print(sol.longestConsecutive([100,4,200,3,2,1]))