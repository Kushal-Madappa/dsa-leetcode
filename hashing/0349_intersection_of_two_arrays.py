# LeetCode: Intersection of Two Arrays (#349)
# https://leetcode.com/problems/intersection-of-two-arrays/
from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        Hash-set intersection: each unique element of nums1 lives in a set;
        every nums2 element checked against it is O(1). Result is the set
        of common values, returned as a list.

        Time:  O(n + m)
        Space: O(min(n, m)) for the result set
        """
        return list(set(nums1) & set(nums2))
