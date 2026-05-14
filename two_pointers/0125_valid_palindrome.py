"""LeetCode 125 — Valid Palindrome (Easy).

Determine whether a string is a palindrome, considering only
alphanumeric characters and ignoring case.

Pattern: two pointers walking inward, skipping non-alphanumeric chars.
This is the canonical "shrink the window from both ends" template.

Time:  O(n) — each character is visited at most once.
Space: O(1) — only two index pointers (no extra string built).
"""

from __future__ import annotations


class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            # Skip non-alphanumeric chars from the left.
            while left < right and not s[left].isalnum():
                left += 1
            # Skip non-alphanumeric chars from the right.
            while left < right and not s[right].isalnum():
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True


def _test() -> None:
    sol = Solution()
    assert sol.isPalindrome("A man, a plan, a canal: Panama") is True
    assert sol.isPalindrome("race a car") is False
    assert sol.isPalindrome(" ") is True
    assert sol.isPalindrome(".,") is True
    # Mixed case alphanumerics: '0' vs 'P' -> not equal -> False.
    assert sol.isPalindrome("0P") is False
    assert sol.isPalindrome("aA") is True
    print("0125_valid_palindrome: all tests passed.")


if __name__ == "__main__":
    _test()
