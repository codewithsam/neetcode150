from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def _subsetsWithDup(start,output):
            nonlocal res
            res.append(output[:])
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]: continue
                output.append(nums[i])
                _subsetsWithDup(i+1, output)
                output.pop()
        _subsetsWithDup(0, [])
        return res

sol = Solution()

print(sol.subsetsWithDup([1,2,1]))
# print(sol.subsetsWithDup([1,2,2]))
# print(sol.subsetsWithDup([7,7]))
# print(sol.subsetsWithDup([1,2,3,1,4]))

