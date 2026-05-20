"""
LeetCode 69 -- Sqrt(x) (Easy)
=============================

Topic: Binary Search ("binary search the answer" / parametric)
URL:   https://leetcode.com/problems/sqrtx/

Problem
-------
Given a non-negative integer `x`, return the integer square root,
i.e. floor(sqrt(x)). No floating-point operators allowed.

Approach -- binary search the answer
------------------------------------
We are not searching an array; we are searching the integer answer
space [0, x] for the largest `r` such that `r * r <= x`. The
predicate `p(r) = (r * r <= x)` is monotonic: it starts True at 0
and eventually becomes False, so we want the *rightmost True*.

Two equivalent formulations:

(a) Closed-interval, "track best so far":
        lo, hi = 0, x
        while lo <= hi:
            mid = (lo + hi) // 2
            if mid * mid <= x:
                ans = mid          # mid is feasible; try bigger
                lo = mid + 1
            else:
                hi = mid - 1       # mid too big; shrink
        return ans

(b) Half-open / upper_bound style (the one used below):
        Find the *leftmost* r with r * r > x; the answer is r - 1.
        Predicate p(r) = (r * r > x).
        lo, hi = 0, x + 1          # the +1 mirrors hi = len in array searches
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if mid * mid > x:
                hi = mid           # candidate "too big" boundary
            else:
                lo = mid + 1       # mid still feasible
        return lo - 1

Both are O(log x). I use (b) here because it makes the link with the
half-open template from #35 and #278 crystal clear: the array is just
"the answer space," and we are doing `lower_bound` on the predicate
`r * r > x`.

Complexity
----------
Time:  O(log x)
Space: O(1)

Edge cases
----------
- x == 0 -> 0
- x == 1 -> 1
- x is a perfect square -> exactly sqrt(x)
- x is large (LeetCode caps x at 2**31 - 1) -> mid * mid stays an
  int in Python; in C/C++/Java you must guard against overflow,
  typically by using `mid > x / mid` instead of `mid * mid > x`.
"""


def my_sqrt(x: int) -> int:
    """Return floor(sqrt(x)) for non-negative integer x."""
    # Find the leftmost r in [0, x+1) with r*r > x; answer is r - 1.
    lo, hi = 0, x + 1
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if mid * mid > x:
            hi = mid
        else:
            lo = mid + 1
    return lo - 1


if __name__ == "__main__":
    # LeetCode official examples
    assert my_sqrt(4) == 2
    assert my_sqrt(8) == 2          # 2*2 = 4 <= 8 < 9 = 3*3

    # Edge cases
    assert my_sqrt(0) == 0
    assert my_sqrt(1) == 1
    assert my_sqrt(2) == 1
    assert my_sqrt(3) == 1
    assert my_sqrt(9) == 3          # perfect square
    assert my_sqrt(15) == 3
    assert my_sqrt(16) == 4
    assert my_sqrt(99) == 9
    assert my_sqrt(100) == 10

    # Large value: LeetCode caps at 2**31 - 1 = 2147483647.
    # floor(sqrt(2147483647)) = 46340.
    assert my_sqrt(2_147_483_647) == 46340

    # Stress against math.isqrt across a sweep of values.
    import math
    for v in [0, 1, 2, 3, 4, 5, 9, 10, 99, 100, 12345, 2**20, 2**30]:
        assert my_sqrt(v) == math.isqrt(v), v
    # Random-ish dense sweep over the low range.
    for v in range(0, 5000):
        assert my_sqrt(v) == math.isqrt(v), v

    print("All tests passed.")
