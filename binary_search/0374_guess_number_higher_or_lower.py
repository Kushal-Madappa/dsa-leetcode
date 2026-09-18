# LeetCode: Guess Number Higher or Lower (#374)
# https://leetcode.com/problems/guess-number-higher-or-lower/

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        lo, hi = 1, n
        while lo <= hi:
            mid = (lo + hi) // 2
            g = guess(mid)
            if g == 0:
                return mid
            elif g < 0:
                hi = mid - 1
            else:
                lo = mid + 1
        return -1
