# LeetCode: Substrings of Size Three with Distinct Characters (#1876)
# https://leetcode.com/problems/substrings-of-size-three-with-distinct-characters/


class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        """
        Fixed-size sliding window of length 3: for each window check that
        the three characters are pairwise distinct. Three comparisons per
        window is O(1) work.

        Time:  O(n)
        Space: O(1)
        """
        count = 0
        for i in range(len(s) - 2):
            if s[i] != s[i + 1] and s[i] != s[i + 2] and s[i + 1] != s[i + 2]:
                count += 1
        return count
