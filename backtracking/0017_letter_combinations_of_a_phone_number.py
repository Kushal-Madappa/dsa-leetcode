# LeetCode: Letter Combinations of a Phone Number (#17)
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        mapping = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz",
        }
        result: List[str] = []
        path: List[str] = []

        def backtrack(i: int) -> None:
            if i == len(digits):
                result.append("".join(path))
                return
            for ch in mapping[digits[i]]:
                path.append(ch)
                backtrack(i + 1)
                path.pop()

        backtrack(0)
        return result
