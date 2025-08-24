from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res  = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                top = stack.pop()
                res[top[1]] = i-top[1]
            stack.append((t, i))
        return res
    
    
    def dailyTemperaturesWithoutStack(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        hottest = -1
        for i in range(len(temperatures)-1, -1, -1):
            if temperatures[i] >= hottest:
                hottest = temperatures[i]
                continue
            days = 1
            while temperatures[i+days] <= temperatures[i]:
                days += res[i+days]
            res[i] = days
        return res

sol = Solution()
print(sol.dailyTemperatures([30,38,30,36,35,40,28]))
print(sol.dailyTemperaturesWithoutStack([30,38,30,36,35,40,28]))