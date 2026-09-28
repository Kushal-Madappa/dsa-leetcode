# LeetCode: Basic Calculator (#224)
# https://leetcode.com/problems/basic-calculator/


class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        result = 0
        num = 0
        sign = 1
        for ch in s:
            if ch.isdigit():
                num = num * 10 + int(ch)
            elif ch == '+':
                result += sign * num
                num = 0
                sign = 1
            elif ch == '-':
                result += sign * num
                num = 0
                sign = -1
            elif ch == '(':
                stack.append(result)
                stack.append(sign)
                result = 0
                sign = 1
            elif ch == ')':
                result += sign * num
                num = 0
                result *= stack.pop()  # sign before '('
                result += stack.pop()  # result before '('
        result += sign * num
        return result
