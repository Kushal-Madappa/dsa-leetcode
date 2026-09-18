# LeetCode: Daily Temperatures (#739)
# https://leetcode.com/problems/daily-temperatures/
from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n
        stack = []
        for i in range(n):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                j = stack.pop()
                result[j] = i - j
            stack.append(i)
        return result
