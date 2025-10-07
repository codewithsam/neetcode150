class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}

        def dp(target):
            if target in memo:
                return memo[target]
            if target < 0:
                return 0
            if target == 0:
                return 1
            if target == 1:
                return 1
            memo[target] = dp(target - 1) + dp(target - 2)
            return memo[target]

        return dp(n)

    def climbStairsWithDP(self, n: int) -> int:
        prev2, prev1 = 0, 1
        for _ in range(n):
            curr = prev1 + prev2
            prev2 = prev1
            prev1 = curr
        return prev1


sol = Solution()

# 1. smallest valid input
# Only one step, so exactly 1 way
print(sol.climbStairs(1))  # expected output: 1

# 2. Two steps
# Ways: (1+1), (2)
print(sol.climbStairs(2))  # expected output: 2

# 3. Three steps
# Ways: (1+1+1), (1+2), (2+1)
print(sol.climbStairs(3))  # expected output: 3

# 4. Four steps
# Ways: 5 (see combinations)
print(sol.climbStairs(4))  # expected output: 5

# 5. Some larger value to test performance
print(sol.climbStairs(10))  # expected output: 89

# 6. Upper bound (according to constraints, n ≤ 45)
print(sol.climbStairs(45))  # expected output: 1836311903


##### _______________________________ ######


# 1. smallest valid input
# Only one step, so exactly 1 way
print(sol.climbStairsWithDP(1))  # expected output: 1

# 2. Two steps
# Ways: (1+1), (2)
print(sol.climbStairsWithDP(2))  # expected output: 2

# 3. Three steps
# Ways: (1+1+1), (1+2), (2+1)
print(sol.climbStairsWithDP(3))  # expected output: 3

# 4. Four steps
# Ways: 5 (see combinations)
print(sol.climbStairsWithDP(4))  # expected output: 5

# 5. Some larger value to test performance
print(sol.climbStairsWithDP(10))  # expected output: 89

# 6. Upper bound (according to constraints, n ≤ 45)
print(sol.climbStairsWithDP(45))  # expected output: 1836311903
