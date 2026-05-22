# Binary Search — Templates & Cheatsheet

Two canonical templates cover ~95% of binary-search problems. The
trick is to **pick one per problem and stay consistent inside the
function** — most off-by-one bugs come from mixing the two.

---

## Template 1 — Closed interval `[lo, hi]`

Use when the question is **"is target here, yes or no?"** and the
answer is a specific cell (or `-1` if absent).

```python
def search(nums, target):
    lo, hi = 0, len(nums) - 1          # closed: hi is the LAST index
    while lo <= hi:                    # interval non-empty while lo <= hi
        mid = lo + (hi - lo) // 2
        if nums[mid] == target:
            return mid                 # found
        if nums[mid] < target:
            lo = mid + 1               # discard left half + mid
        else:
            hi = mid - 1               # discard right half + mid
    return -1                          # exhausted
```

Worked example: **LC #704 Binary Search** — `0704_binary_search.py`.

---

## Template 2 — Half-open interval `[lo, hi)` (leftmost-true / lower_bound)

Use when the question is **"what is the leftmost index where some
predicate `p(i)` becomes true?"**. The answer is always defined
(possibly `len(nums)` if no index satisfies `p`).

```python
def lower_bound(nums, target):
    lo, hi = 0, len(nums)              # half-open: hi == len(nums)
    while lo < hi:                     # interval non-empty while lo < hi
        mid = lo + (hi - lo) // 2
        if nums[mid] >= target:        # predicate p(mid)
            hi = mid                   # KEEP mid as a candidate
        else:
            lo = mid + 1               # discard mid
    return lo                          # lo == hi == answer
```

Worked example: **LC #35 Search Insert Position** — `0035_search_insert_position.py`.

---

## Choosing between them

| Question shape                              | Template            |
|---------------------------------------------|---------------------|
| "Find this exact value, else -1."           | Closed `[lo, hi]`   |
| "Leftmost index where `p` is true."         | Half-open `[lo, hi)`|
| "Rightmost index where `p` is true."        | Half-open mirrored  |
| "Smallest `x` such that something holds."   | Half-open (parametric search) |

Rule of thumb: if the answer might land **one past the last index**,
use the half-open template — `hi = len(nums)` naturally encodes
"insert at the end".

---

## Common pitfalls

- **Mixing the two templates inside one function**. Pick one and
  commit. Mixing produces infinite loops or off-by-ones.
- **Forgetting `+ 1` / `- 1`** when updating `lo` / `hi` in the
  closed template. Both bounds must always shrink, or you'll loop
  forever.
- **Off-by-one on `hi`**: in the closed template `hi = len(nums) - 1`;
  in the half-open `hi = len(nums)`. Match the convention.
- **Overflow on `(lo + hi) // 2`** — non-issue in Python, but write
  `lo + (hi - lo) // 2` anyway; the muscle memory ports cleanly to
  C / C++ / Java.

---

## What comes next

Once these two templates are reflex, the natural follow-ups are:

- LC #34 — Find First and Last Position (lower_bound + upper_bound).
- LC #33 / #81 — Search in Rotated Sorted Array (template + a
  case-split on which half is sorted).
- LC #278 — First Bad Version (pure leftmost-true).
- LC #74 — Search a 2D Matrix (binary-search on flattened index).
- LC #162 — Find Peak Element (binary-search on a predicate that
  isn't about a target value).

The shape stays the same; only the predicate changes.

## Day 10 (2026-05-21)

- Added #278, #34, #69, #367 — predicates over the answer space.
