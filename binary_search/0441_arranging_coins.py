# LeetCode: Arranging Coins (#441)
# https://leetcode.com/problems/arranging-coins/


class Solution:
    def arrangeCoins(self, n: int) -> int:
        lo, hi = 0, n
        while lo <= hi:
            mid = (lo + hi) // 2
            coins = mid * (mid + 1) // 2
            if coins == n:
                return mid
            if coins < n:
                lo = mid + 1
            else:
                hi = mid - 1
        return hi
