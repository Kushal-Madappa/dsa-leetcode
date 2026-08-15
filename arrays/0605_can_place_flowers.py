# LeetCode: Can Place Flowers (#605)
# https://leetcode.com/problems/can-place-flowers/
from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        count = 0
        i = 0
        length = len(flowerbed)
        while i < length:
            if flowerbed[i] == 0:
                prev_empty = (i == 0) or (flowerbed[i - 1] == 0)
                next_empty = (i == length - 1) or (flowerbed[i + 1] == 0)
                if prev_empty and next_empty:
                    flowerbed[i] = 1
                    count += 1
                    if count >= n:
                        return True
                    i += 2
                    continue
            i += 1
        return count >= n
