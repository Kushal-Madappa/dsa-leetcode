"""
LeetCode #3 — Longest Substring Without Repeating Characters
Difficulty  : Medium
Topic tags  : Sliding Window (Variable Size), Hashing, Strings
---------------------------------------------------------------
Problem
-------
Given a string s, find the length of the longest substring that contains
no repeating characters.

Approach — Variable-size sliding window with a hash map
--------------------------------------------------------
Maintain a window [left, right] and a dict {char: last_seen_index}.

For each new character s[right]:
  - If it was seen before AND its last index is inside the current window
    (>= left), jump left to last_index + 1, instantly collapsing the window
    past the duplicate.  No inner while-loop needed.
  - Update last_seen[s[right]] = right.
  - Update best = max(best, right - left + 1).

Why the dict beats a set:
  A set requires an O(window_size) while-loop shrink to evict the duplicate.
  The dict gives O(1) jump: we know exactly where to move left.

Complexity
----------
  Time  : O(n)  — each character visited at most twice (once by right,
                  once implicitly skipped by the left jump)
  Space : O(min(n, |alphabet|))  — at most 128 entries for ASCII
"""


def lengthOfLongestSubstring(s: str) -> int:
    """Return the length of the longest substring without repeating chars."""
    last_seen: dict[str, int] = {}  # char -> most recent index
    best: int = 0
    left: int = 0

    for right, ch in enumerate(s):
        # if ch is inside the current window, jump left past it
        if ch in last_seen and last_seen[ch] >= left:
            left = last_seen[ch] + 1
        last_seen[ch] = right
        window_len = right - left + 1
        if window_len > best:
            best = window_len

    return best


# self-test
if __name__ == "__main__":
    assert lengthOfLongestSubstring("abcabcbb") == 3   # "abc"
    assert lengthOfLongestSubstring("bbbbb") == 1      # "b"
    assert lengthOfLongestSubstring("pwwkew") == 3     # "wke"
    assert lengthOfLongestSubstring("") == 0
    assert lengthOfLongestSubstring("au") == 2
    assert lengthOfLongestSubstring("dvdf") == 3       # "vdf"
    print("All tests passed")
