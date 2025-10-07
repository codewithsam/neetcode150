from typing import List


class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        operands = ["+", "-", "*", "/"]
        EPSILON = 1e-6
        found = False

        def _backtrack(candidates):
            nonlocal found
            if len(candidates) == 1:
                if abs(candidates[0] - 24) < EPSILON:
                    found = True

            if found:
                return
            n = len(candidates)
            for i in range(n):
                for j in range(i + 1, n):
                    op1, op2 = candidates[i], candidates[j]

                    remaining_candidates = [candidates[k] for k in range(n) if k != i and k != j]
                    for op in operands:
                        if op == "+":
                            total = op1 + op2
                            remaining_candidates.append(total)
                            _backtrack(remaining_candidates)
                            remaining_candidates.pop()
                        elif op == "-":
                            total = op1 - op2
                            remaining_candidates.append(total)
                            _backtrack(remaining_candidates)
                            remaining_candidates.pop()

                            total = op2 - op1
                            remaining_candidates.append(total)
                            _backtrack(remaining_candidates)
                            remaining_candidates.pop()
                        elif op == "*":
                            total = op1 * op2
                            remaining_candidates.append(total)
                            _backtrack(remaining_candidates)
                            remaining_candidates.pop()
                        else:
                            if abs(op2) > EPSILON:
                                total = op1 / op2
                                remaining_candidates.append(total)
                                _backtrack(remaining_candidates)
                                remaining_candidates.pop()

                            if abs(op1) > EPSILON:
                                total = op2 / op1
                                remaining_candidates.append(total)
                                _backtrack(remaining_candidates)
                                remaining_candidates.pop()

        _backtrack(cards)
        return found


sol = Solution()
print(sol.judgePoint24([4, 1, 8, 7]))
