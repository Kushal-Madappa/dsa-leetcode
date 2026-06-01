# LeetCode: Majority Element (#169)
# https://leetcode.com/problems/majority-element/
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Boyer-Moore voting: maintain a candidate and a count.
        # When count hits 0, adopt the current number as the new candidate.
        candidate = 0
        count = 0
        for n in nums:
            if count == 0:
                candidate = n
            count += 1 if n == candidate else -1
        return candidate
