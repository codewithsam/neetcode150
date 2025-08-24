class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0 or len(s) == 1: return False
        stack = []
        pairs = {'(': ')', '{': '}', '[': ']'}
        for bracket in s:
            if bracket in pairs:
                stack.append(bracket)
            elif len(stack) <= 0 or bracket != pairs[stack[-1]]:
                return False
            else:
                if len(stack) > 0: stack.pop()
        return True if len(stack) == 0 else False
    

sol = Solution()
# print(sol.isValid("([{}])"))
# print(sol.isValid("[(])"))
print(sol.isValid("]"))
print(sol.isValid("){"))

