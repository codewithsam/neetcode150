class Solution:
    def canSum(self, target, nums):
        def backtrack(goal, nums, memo={}):
            if goal in memo:
                return memo[goal]
            if goal == 0:
                return True
            if goal < 0:
                return False

            for num in nums:
                if backtrack(goal - num, nums, memo):
                    memo[goal] = True
                    return True
            memo[goal] = False

        return backtrack(target, nums)


sol = Solution()

print(sol.canSum(7, [2, 3]))  # True
print(sol.canSum(7, [5, 3, 4, 7]))  # True
print(sol.canSum(7, [2, 4]))  # False
print(sol.canSum(8, [2, 3, 5]))  # True
print(sol.canSum(300, [7, 14]))  # True
