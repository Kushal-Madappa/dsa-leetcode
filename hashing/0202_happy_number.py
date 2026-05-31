# LeetCode: Happy Number (#202)
# https://leetcode.com/problems/happy-number/


class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            total = 0
            while n > 0:
                n, d = divmod(n, 10)
                total += d * d
            n = total
        return n == 1
