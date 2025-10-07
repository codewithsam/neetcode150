class Solution:
    def gridTraveller(self, m, n, memo={}):
        if (m, n) in memo:
            return memo[(m, n)]
        if m == 0 or n == 0:
            return 0
        if m == 1 and n == 1:
            return 1
        memo[(m, n)] = self.gridTraveller(m - 1, n, memo) + self.gridTraveller(m, n - 1, memo)
        return memo[(m, n)]


sol = Solution()

print(sol.gridTraveller(1, 1))
print(sol.gridTraveller(2, 3))
print(sol.gridTraveller(3, 2))
print(sol.gridTraveller(3, 3))
print(sol.gridTraveller(18, 18))
