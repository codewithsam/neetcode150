from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def _combinationSum(start,goal, output):
            nonlocal res
            if goal == 0:
                res.append(output[:])
                return
            if goal < 0:
                return
            for i in range(start, len(candidates)):
                if i>start and candidates[i] == candidates[i-1]: continue
                output.append(candidates[i])
                _combinationSum(i+1,goal-candidates[i], output)
                output.pop()
        
        _combinationSum(0, target, [])
        return res

sol = Solution()
print(sol.combinationSum2([1,1,2,5,6,7,10], 8)) # [1,1,2,5,6,7,10]