# LeetCode: Minimum Flips to Make a OR b Equal to c (#1318)
# https://leetcode.com/problems/minimum-flips-to-make-a-or-b-equal-to-c/


class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        flips = 0
        while a or b or c:
            ab = a & 1
            bb = b & 1
            cb = c & 1
            if cb == 1:
                if ab == 0 and bb == 0:
                    flips += 1
            else:
                flips += ab + bb
            a >>= 1
            b >>= 1
            c >>= 1
        return flips
