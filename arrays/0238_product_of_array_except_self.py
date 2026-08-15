# LeetCode: Product of Array Except Self (#238)
# https://leetcode.com/problems/product-of-array-except-self/
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n
        # First pass: prefix products (product of all elements to the left of i)
        left = 1
        for i in range(n):
            result[i] = left
            left *= nums[i]
        # Second pass: multiply by suffix products (product of all elements to the right of i)
        right = 1
        for i in range(n - 1, -1, -1):
            result[i] *= right
            right *= nums[i]
        return result
