# LeetCode: Intersection of Two Arrays II (#350)
# https://leetcode.com/problems/intersection-of-two-arrays-ii/
from typing import List
from collections import Counter


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counts = Counter(nums1)
        result = []
        for n in nums2:
            if counts[n] > 0:
                result.append(n)
                counts[n] -= 1
        return result
