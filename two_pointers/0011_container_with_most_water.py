# LeetCode: Container With Most Water (#11)
# https://leetcode.com/problems/container-with-most-water/

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        best = 0
        while left < right:
            h = min(height[left], height[right])
            area = h * (right - left)
            if area > best:
                best = area
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return best
