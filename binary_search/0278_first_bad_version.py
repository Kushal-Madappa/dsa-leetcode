"""
LeetCode 278 -- First Bad Version (Easy)
========================================

Topic: Binary Search (leftmost-true / lower_bound on a predicate)
URL:   https://leetcode.com/problems/first-bad-version/

Problem
-------
You are a product manager. n versions are numbered 1..n. After a
bad version, every subsequent version is also bad. You are given an
API `isBadVersion(v) -> bool`. Find the first bad version, calling
the API as few times as possible.

Approach
--------
This is the purest form of the half-open / leftmost-true template:
the predicate is given to us already (`isBadVersion`). The sequence
`isBadVersion(1), isBadVersion(2), ...` is monotonic: once it flips
to True, it stays True. So the "first bad" is the leftmost index
where the predicate is True -- a `lower_bound` over a predicate.

    Invariant: the answer lies in the half-open interval [lo, hi].
               (We initialise hi = n because at least one version
               is bad, so the answer is guaranteed in 1..n; we use
               hi = n exclusive of `n + 1`.)
    Loop:      while lo < hi.
    Update:    if isBadVersion(mid): hi = mid     # mid is candidate
               else:                  lo = mid + 1 # mid is good

When the loop exits, lo == hi == first bad version. The number of
API calls is O(log n).

Complexity
----------
Time:  O(log n) API calls
Space: O(1)

Edge cases
----------
- Bad version is 1 -- the loop converges to lo = 1.
- Bad version is n -- every check returns False until mid = n; the
  loop still converges in O(log n).
- n == 1 -- the loop body never runs; we return 1 (the only
  candidate). The problem guarantees at least one bad version.
"""

from typing import Callable


def first_bad_version(n: int, is_bad_version: Callable[[int], bool]) -> int:
    """Return the smallest v in [1, n] with is_bad_version(v) True."""
    lo, hi = 1, n                # half-open style on a 1-indexed range
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if is_bad_version(mid):
            hi = mid             # mid is a candidate first-bad
        else:
            lo = mid + 1         # mid is good, skip past it
    return lo


# LeetCode wraps isBadVersion as a closure; we replicate that here
# so the file is self-contained and testable in plain Python.
def _make_oracle(first_bad: int) -> Callable[[int], bool]:
    """Return an isBadVersion(v) closure with the given threshold."""
    return lambda v: v >= first_bad


if __name__ == "__main__":
    # Official LeetCode example: n=5, bad=4 -> 4
    assert first_bad_version(5, _make_oracle(4)) == 4

    # Edge: only one version, and it is bad
    assert first_bad_version(1, _make_oracle(1)) == 1

    # Edge: first version is bad
    assert first_bad_version(10, _make_oracle(1)) == 1

    # Edge: last version is bad
    assert first_bad_version(10, _make_oracle(10)) == 10

    # Edge: large n -- confirm correctness across the whole range
    N = 10_000
    for k in (1, 2, 17, 5000, N - 1, N):
        assert first_bad_version(N, _make_oracle(k)) == k, k

    # Sanity: counted API calls should be O(log n)
    import math
    for k in (1, 5000, N):
        calls = {"n": 0}
        def oracle(v, k=k, calls=calls):
            calls["n"] += 1
            return v >= k
        first_bad_version(N, oracle)
        # ceil(log2(N)) + a small slack; 14 is plenty for N=10000.
        assert calls["n"] <= math.ceil(math.log2(N)) + 2, (k, calls["n"])

    print("All tests passed.")
