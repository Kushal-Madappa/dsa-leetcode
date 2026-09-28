# LeetCode: Zigzag Conversion (#6)
# https://leetcode.com/problems/zigzag-conversion/


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        rows = [[] for _ in range(numRows)]
        cur = 0
        step = 1
        for ch in s:
            rows[cur].append(ch)
            if cur == 0:
                step = 1
            elif cur == numRows - 1:
                step = -1
            cur += step
        return "".join("".join(r) for r in rows)
