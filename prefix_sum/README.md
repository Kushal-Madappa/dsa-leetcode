# Prefix Sum — when (and when not) to use it

A prefix sum array `P` over `nums` is defined as

```
P[0] = 0
P[i] = nums[0] + nums[1] + ... + nums[i-1]
```

so that **any range sum** becomes O(1):

```
sum(nums[l..r]) = P[r+1] - P[l]
```

That one identity is the engine for a surprising number of patterns.

## When prefix sums *beat* sliding window

Sliding window needs the invariant *"shrinking the window monotonically
improves the metric"*. That invariant **breaks the moment the array can
contain negatives**, because shrinking can *increase* the sum.

| Situation | Prefer |
|-----------|--------|
| All values non-negative, contiguous-subarray metric | Sliding window (O(1) extra space) |
| Values can be negative / zero | Prefix sum + hash map |
| Many range-sum queries on a fixed array | Prefix sum (precompute once) |
| Count subarrays with a *property of the sum* (e.g. `== k`, `% k == 0`, XOR `== k`) | Prefix sum + hash map |

## The "running value + map" family

All of these share one skeleton:

```python
counts = defaultdict(int)
counts[seed] = 1                # empty-prefix sentinel
running = identity_value
for x in nums:
    running = combine(running, x)
    answer += counts[target_complement(running)]
    counts[running] += 1
```

Swap `combine` / `target_complement` and a whole family appears:

| Pattern | `combine` | `target_complement(running)` | Example |
|---------|-----------|------------------------------|---------|
| Sum == k | `running + x` | `running - k` | LC #560 |
| Sum divisible by k | `(running + x) % k` | `running` (same remainder) | LC #974 |
| Longest sum == k | `running + x` (store first index) | `running - k` | LC #325 |
| First index, sum divisible by k, length >= 2 | `(running + x) % k` (store first index) | `running` | LC #523 |
| XOR == k | `running ^ x` | `running ^ k` | LC #1442 |

The `counts[0] = 1` seed (or `first_index[0] = -1`) is what lets
subarrays that *start at index 0* get counted — they correspond to the
empty prefix `P[0] = 0`.

## Negative-mod gotcha

For "sum divisible by k" the key is `running % k`. In Python this is
already non-negative for positive `k`:

```python
(-3) % 5 == 2     # Python
```

In C++/Java you must normalise:

```cpp
int key = ((running % k) + k) % k;
```

## Two distinct uses

There are really two flavours of prefix sums:

1. **Array as a precomputed data structure** — build once, answer many
   range-sum queries in O(1). LC #303 is the canonical example.
2. **Streaming + hash map** — walk left to right, registering each
   running value as you go, and *querying* the map for the complement
   that closes a valid subarray. LC #560 / #974 / #1442 are this
   flavour.

Internalise both — they look similar but are used differently.

## Solutions in this folder
- `0303_range_sum_query_immutable.py` — Easy, "build once, query forever".
- `0560_subarray_sum_equals_k.py` — Medium, the canonical prefix-sum + hash map.
- `0724_find_pivot_index.py` — Easy, prefix sum from both sides on the fly.
- `0974_subarray_sums_divisible_by_k.py` — Medium, key = `prefix % k`.
