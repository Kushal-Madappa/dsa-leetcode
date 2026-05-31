# LeetCode: Merge Sorted Array (#88)
# https://leetcode.com/problems/merge-sorted-array/
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.

        Three-pointer merge from the back: place the larger of nums1[i] and
        nums2[j] at nums1[k], moving the pointer for the chosen side.
        Filling from the tail avoids overwriting unprocessed nums1 values.

        Time:  O(m + n)
        Space: O(1)
        """
        i, j, k = m - 1, n - 1, m + n - 1
        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
