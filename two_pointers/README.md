# Two Pointers

Two pointers is the go-to pattern whenever you can reduce a 2D search
(every pair) to a single sweep by exploiting structure in the input —
usually sortedness or a monotone relationship between the pointers.

## Variants

1. **Opposite ends, converging.** Start `left = 0`, `right = n - 1`,
   move whichever pointer makes the invariant improve.
   - LeetCode 167 — Two Sum II (sorted array, target sum)
   - LeetCode 125 — Valid Palindrome (skip non-alnum, compare chars)
   - LeetCode 11 — Container With Most Water (move the shorter side)
   - LeetCode 15 — 3Sum (fix one index, two-pointer the rest)

2. **Same direction (fast / slow).** Used for in-place rewrites and
   cycle detection.
   - LeetCode 26 — Remove Duplicates from Sorted Array
   - LeetCode 283 — Move Zeroes
   - LeetCode 141 — Linked List Cycle (Floyd's tortoise & hare)

3. **Sliding window.** A specialised two-pointer pattern where both
   pointers move forward and you maintain a running aggregate.

## When to reach for it

- The problem mentions "sorted" or you can afford an O(n log n) sort up
  front.
- You're tempted to write a nested loop comparing pairs.
- You need O(1) extra space.

## Complexity cheat-sheet

| Variant            | Time   | Space |
|--------------------|--------|-------|
| Opposite ends      | O(n)   | O(1)  |
| Fast / slow        | O(n)   | O(1)  |
| Sliding window     | O(n)   | O(k)  |
