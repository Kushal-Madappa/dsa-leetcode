# LeetCode: Combination Sum III (#216)
# https://leetcode.com/problems/combination-sum-iii/
from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []

        def backtrack(start: int, path: List[int], remaining: int) -> None:
            if len(path) == k:
                if remaining == 0:
                    result.append(path[:])
                return
            for num in range(start, 10):
                if num > remaining:
                    break
                path.append(num)
                backtrack(num + 1, path, remaining - num)
                path.pop()

        backtrack(1, [], n)
        return result
