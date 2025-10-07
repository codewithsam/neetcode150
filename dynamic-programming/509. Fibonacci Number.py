class Solution:
    def fib(self, n: int) -> int:
        dp = {}

        def calcFib(n):
            if n in dp:
                return dp[n]

            if n == 0:
                return 0
            if n == 1 or n == 2:
                return 1

            dp[n] = calcFib(n - 1) + calcFib(n - 2)

            return dp[n]

        return calcFib(n)


sol = Solution()

print(sol.fib(5))
print(sol.fib(8))
print(sol.fib(50))
