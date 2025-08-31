from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def _combinationSum(start,goal, output):
            nonlocal res
            if goal == 0:
                res.append(output[:])
                return
            if goal < 0:
                return
            for i in range(start, len(candidates)):
                output.append(candidates[i])
                _combinationSum(i,goal-candidates[i], output)
                output.pop()
        _combinationSum(0, target, [])
        return res
    
sol = Solution()
print(sol.combinationSum([2,3,6,7], 7))