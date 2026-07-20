# LeetCode: Minimum Recolors to Get K Consecutive Black Blocks (#2379)
# https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/


class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        whites = blocks[:k].count('W')
        best = whites
        for i in range(k, len(blocks)):
            whites += (blocks[i] == 'W') - (blocks[i - k] == 'W')
            if whites < best:
                best = whites
        return best
