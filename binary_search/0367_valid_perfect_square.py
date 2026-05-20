"""
LeetCode 367 -- Valid Perfect Square (Easy)
==========================================

Topic: Binary Search ("binary search the answer")
URL:   https://leetcode.com/problems/valid-perfect-square/

Problem
-------
Given a positive integer `num`, return True iff it is a perfect
square (i.e. exists an integer r with r * r == num). Do not use any
built-in like `sqrt`.

Approach
--------
Binary search the integer `r` in [1, num] for the predicate
`r * r == num`. The function `r -> r * r` is strictly monotonic for
r >= 0, so a standard closed-interval binary search works directly:

    lo, hi = 1, num
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        sq = mid * mid
        if sq == num: return True
        if sq <  num: lo = mid + 1
        else:         hi = mid - 1
    return False

This is the natural sibling of #69 (Sqrt(x)): same monotonic
answer-space search, but the question we ask is "exactly equal?"
rather than "what's the floor?".

Complexity
----------
Time:  O(log num)
Space: O(1)

Edge cases / pitfalls
---------------------
- num == 1 -> True (1 * 1 == 1). Initialising lo = 1 handles this.
- Large num: LeetCode caps num at 2**31 - 1; Python ints don't
  overflow. In C/C++/Java, prefer `mid > num / mid` to avoid
  overflow on `mid * mid`.
- Common mistake: using `mid = (lo + hi) // 2` is fine in Python
  but unsafe in fixed-width languages near INT_MAX -- the
  `lo + (hi - lo) // 2` form is the portable one.
"""


def is_perfect_square(num: int) -> bool:
    """Return True iff `num` is a positive integer perfect square."""
    if num < 1:
        return False
    lo, hi = 1, num
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        sq = mid * mid
        if sq == num:
            return True
        if sq < num:
            lo = mid + 1
        else:
            hi = mid - 1
    return False


if __name__ == "__main__":
    # LeetCode official examples
    assert is_perfect_square(16) is True
    assert is_perfect_square(14) is False

    # Smallest perfect square
    assert is_perfect_square(1) is True

    # Small non-squares
    for n in [2, 3, 5, 6, 7, 8, 10, 15, 17, 99]:
        assert is_perfect_square(n) is False, n

    # Small perfect squares
    for r in range(1, 50):
        assert is_perfect_square(r * r) is True, r

    # Boundary near LeetCode constraint (1 <= num <= 2**31 - 1).
    # 46340 ** 2 = 2_147_395_600 (largest square <= 2**31 - 1).
    assert is_perfect_square(46340 * 46340) is True
    assert is_perfect_square(46340 * 46340 + 1) is False
    assert is_perfect_square(2_147_483_647) is False  # = 2**31 - 1, not a square

    # Stress: cross-check against math.isqrt for a dense range.
    import math
    for n in range(1, 5000):
        expected = (math.isqrt(n) ** 2 == n)
        assert is_perfect_square(n) == expected, n

    print("All tests passed.")
