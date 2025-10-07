class Solution:
    def fib(self, n, memo={}):
        if n in memo:
            return memo[n]
        if n <= 2:
            return 1
        memo[n] = self.fib(n - 1) + self.fib(n - 2)
        return memo[n]


sol = Solution()


print(sol.fib(6))
print(sol.fib(7))
print(sol.fib(8))
print(sol.fib(50))
