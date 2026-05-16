"""
LeetCode #15 — 3Sum
Difficulty: Medium
Topics: Array, Two Pointers, Sorting

Pattern — "sort + fix one + two-pointer the rest":
  1. Sort the array.  (enables two-pointer and easy duplicate skipping)
  2. For each index i, treat nums[i] as the fixed first element and
     find pairs in nums[i+1 .. n-1] that sum to -nums[i].
  3. Two-pointer on the sorted subarray: if sum < target → left++,
     if sum > target → right--, if equal → record and skip duplicates.

Deduplication:
  - Skip nums[i] if it equals nums[i-1]  (same first element → same triplets)
  - After recording a triplet, advance L past duplicate values, R back
    past duplicate values, then take one more step each.

Early exit: once nums[i] > 0, no triplet can sum to 0 (all remaining
elements are ≥ nums[i] > 0).

Time:  O(n²)       — O(n log n) sort + O(n) two-pointer per element
Space: O(1)        — not counting the output list (sort is in-place)
"""

from typing import List


def three_sum(nums: List[int]) -> List[List[int]]:
    """Return all unique triplets [a, b, c] with a + b + c == 0.

    Args:
        nums: Integer list (may contain duplicates, any sign).

    Returns:
        List of unique triplets; order of triplets and order within each
        triplet are both ascending (guaranteed by the sort).
    """
    nums.sort()
    result: List[List[int]] = []
    n = len(nums)

    for i in range(n - 2):
        # Skip duplicate fixed element
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        # All remaining elements ≥ nums[i] > 0 → impossible to reach 0
        if nums[i] > 0:
            break

        left, right = i + 1, n - 1
        target = -nums[i]

        while left < right:
            s = nums[left] + nums[right]
            if s == target:
                result.append([nums[i], nums[left], nums[right]])
                # Skip duplicates on both ends before next step
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
            elif s < target:
                left += 1
            else:
                right -= 1

    return result


# ---------------------------------------------------------------------------
# Self-tests
# ---------------------------------------------------------------------------

def _sorted_set(triplets: List[List[int]]):
    """Canonical form for comparison regardless of output order."""
    return sorted(map(tuple, triplets))


def _test() -> None:
    # Standard example
    assert _sorted_set(three_sum([-1, 0, 1, 2, -1, -4])) == [
        (-1, -1, 2), (-1, 0, 1)
    ]

    # No valid triplet
    assert three_sum([0, 1, 1]) == []

    # All zeros
    assert three_sum([0, 0, 0]) == [[0, 0, 0]]

    # Empty / too short
    assert three_sum([]) == []
    assert three_sum([1, 2]) == []

    # Multiple duplicates
    assert _sorted_set(three_sum([-2, 0, 0, 2, 2])) == [(-2, 0, 2)]

    # All negatives
    assert three_sum([-5, -4, -3, -2, -1]) == []

    print("All tests passed ✓")


if __name__ == "__main__":
    _test()
