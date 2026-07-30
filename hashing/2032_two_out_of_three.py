# LeetCode: Two Out of Three (#2032)
# https://leetcode.com/problems/two-out-of-three/
from typing import List


class Solution:
    def twoOutOfThree(
        self, nums1: List[int], nums2: List[int], nums3: List[int]
    ) -> List[int]:
        s1, s2, s3 = set(nums1), set(nums2), set(nums3)
        return list((s1 & s2) | (s2 & s3) | (s1 & s3))
