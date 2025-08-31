from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def _combinations(input,output):
            nonlocal res
            res.append(output[:])
            for i in range(input, len(nums)):
                output.append(nums[i])
                _combinations(i+1,output)
                output.pop()

        _combinations(0,[])
        return res


sol = Solution()
print(sol.subsets([1,2,3]))