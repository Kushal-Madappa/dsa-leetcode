# LeetCode: Evaluate Reverse Polish Notation (#150)
# https://leetcode.com/problems/evaluate-reverse-polish-notation/
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for tok in tokens:
            if tok in ("+", "-", "*", "/"):
                b = stack.pop()
                a = stack.pop()
                if tok == "+":
                    stack.append(a + b)
                elif tok == "-":
                    stack.append(a - b)
                elif tok == "*":
                    stack.append(a * b)
                else:
                    # Truncate toward zero
                    stack.append(int(a / b))
            else:
                stack.append(int(tok))
        return stack[0]
