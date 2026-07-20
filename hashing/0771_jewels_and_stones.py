# LeetCode: Jewels and Stones (#771)
# https://leetcode.com/problems/jewels-and-stones/


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewel_set = set(jewels)
        return sum(c in jewel_set for c in stones)
