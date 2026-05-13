# dsa-leetcode

My personal LeetCode solution log. Solutions are written in **Python 3** with
a focus on clean code, optimized complexity, and clear explanations -- the
same style I'd use in an interview.

Each file follows a consistent template:

- Problem statement (concise)
- Approach + why it works
- Time / space complexity
- Tested examples runnable via `python <file>.py`

## Structure

```
dsa-leetcode/
├── arrays/       # Array, two-pointer, prefix-sum, sliding window
├── strings/      # String manipulation, hashing on strings
├── hashing/      # Pure hash-map / hash-set patterns
├── trees/        # Binary trees, BSTs, traversal patterns
├── graphs/       # BFS, DFS, Union-Find
├── dp/           # Dynamic programming
└── sql/          # LeetCode SQL problems
```

## Solution log

| # | Problem | Difficulty | Topic(s) | File |
|---|---------|------------|----------|------|
| 1 | Two Sum | Easy | Array, Hash Table | [arrays/0001_two_sum.py](arrays/0001_two_sum.py) |
| 242 | Valid Anagram | Easy | String, Hash Table | [strings/0242_valid_anagram.py](strings/0242_valid_anagram.py) |

## Running

```bash
python arrays/0001_two_sum.py
python strings/0242_valid_anagram.py
```

Each file includes self-contained assertions; a clean run prints
`All tests passed.`
