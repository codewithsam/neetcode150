from typing import List

class Solution:
    def calculate(self, rop, lop, expression):
        match expression:
            case "+":
                return lop+rop
            case "-":
                return lop-rop
            case "*":
                return lop*rop
            case "/":
                return int(lop/rop)
            
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1: return int(tokens[0])
        operators = {"+", "-", "/", "*"}
        stack = []
        
        for token in tokens:
            if token in operators:
                current_result = self.calculate(int(stack.pop()), int(stack.pop()), token)
                stack.append(current_result)
            else:
                stack.append(token)
        return stack[0]

sol = Solution()

print(sol.evalRPN(["1","2","+","3","*","4","-"]))
print(sol.evalRPN(["0","3","/"]))
print(sol.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))