from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        used = [False for _ in nums]
        def _permute(output):
            nonlocal res, used
            if len(output) == len(nums): 
                res.append(output[:])
                return
            for i in range(len(nums)):
                if used[i]: continue
                used[i] = True
                output.append(nums[i])
                _permute(output)
                output.pop()
                used[i] = False
        _permute([])
        return res

sol = Solution()
res = sol.permute([1,2,3,4])
print(res)
print(len(res))
