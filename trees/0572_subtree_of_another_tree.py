"""
LeetCode #572 — Subtree of Another Tree (Easy)
URL: https://leetcode.com/problems/subtree-of-another-tree/

Topic tags : Tree, DFS, Binary Tree, Hashing, String Matching
Pattern    : Nested recursion — outer DFS walks every node in `root`; at each
             node it calls an *inner* recursion (the #100 Same Tree helper) to
             check whether the subtree rooted there is identical to `subRoot`.

Idea
----
"Is `subRoot` a subtree of `root`?" decomposes into two questions we already
know how to answer:

    1. (Outer) Visit every node `n` in `root` until we find one where ...
    2. (Inner) ... the subtree rooted at `n` is *identical* to `subRoot`.

The inner check is exactly LC #100 (Same Tree): two trees match iff both are
empty, or both are non-empty with equal values AND their left and right
children pairwise match. The outer walk is a plain pre-order DFS that
short-circuits as soon as one match is found.

Why nested recursion (and not just one DFS)?
--------------------------------------------
Subtree identity is a *whole-shape* property, not a local property. You
cannot decide it from a constant amount of work at each outer node. So the
outer DFS *delegates* to a second recursion that walks the matching candidate
in lockstep with `subRoot`. The two recursions traverse different things:
outer walks `root`; inner walks (a subtree of `root`) zipped with `subRoot`.

Edges & gotchas
---------------
- **An empty `subRoot` is a subtree of every tree.** LeetCode's constraints
  guarantee both trees have at least one node, but the helper still handles
  the both-None base case correctly, which keeps the recursion clean.
- **Value match isn't enough — structure must match too.** `(1, [2,null,3])`
  vs. `(1, [2,3])` differ in shape; the inner helper catches this because
  one side hits `None` while the other still has a node.
- **Subtree means "complete subtree from some node down,"** not "any
  connected subgraph." So at each outer node we compare the *entire* subtree
  rooted there, not a partial match.

Complexity
----------
- Time : O(m * n) — worst case we run the inner Same Tree (O(m)) at every
         outer node (O(n)). Hashing / string-serialization variants can hit
         O(m + n), but the plain nested recursion is clearest and stays well
         within the LC limits for Easy.
- Space: O(h_root + h_sub) for the two recursion stacks, where h_* is the
         height of each tree. Worst case O(n + m) for fully skewed trees;
         O(log n + log m) for balanced trees.
"""

from typing import Optional


# LeetCode supplies TreeNode automatically. Defined here ONLY so the local
# test block below runs as a standalone Python file — DO NOT paste this
# class into the LeetCode editor.
class TreeNode:
    def __init__(self, val: int = 0,
                 left: "Optional[TreeNode]" = None,
                 right: "Optional[TreeNode]" = None):
        self.val = val
        self.left = left
        self.right = right


# =============================================================================
# Paste THIS class into LeetCode (everything from `class Solution:` through
# the final `return ...`). The TreeNode above and the test block below are
# local-only scaffolding.
# =============================================================================
class Solution:
    def isSubtree(self, root: Optional[TreeNode],
                  subRoot: Optional[TreeNode]) -> bool:
        # ----- Inner recursion: identical-tree check (LC #100 Same Tree) -----
        def same(a: Optional[TreeNode], b: Optional[TreeNode]) -> bool:
            # Both empty => trivially identical.
            if a is None and b is None:
                return True
            # Exactly one empty => shapes differ.
            if a is None or b is None:
                return False
            # Both non-empty: values must match AND children must match.
            return (a.val == b.val
                    and same(a.left, b.left)
                    and same(a.right, b.right))

        # ----- Outer recursion: walk every node in `root` -----
        if root is None:
            # An empty `root` cannot contain a non-empty `subRoot`.
            # (Per LC constraints subRoot is non-empty.)
            return False
        if same(root, subRoot):
            return True
        # Short-circuit: as soon as either subtree contains it, we're done.
        return (self.isSubtree(root.left, subRoot)
                or self.isSubtree(root.right, subRoot))


# =============================================================================
# Local tests (do NOT paste into LeetCode)
# =============================================================================
def _build(values):
    """Build a binary tree from a level-order list with None for missing nodes.
    Mirrors LeetCode's input format, e.g. [3,4,5,1,2] -> the standard tree."""
    if not values:
        return None
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    while queue and i < len(values):
        node = queue.pop(0)
        # Left child
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        # Right child
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root


if __name__ == "__main__":
    sol = Solution()

    cases = [
        # ---- LeetCode official samples ----
        # Example 1: subRoot = [4,1,2] IS a subtree of [3,4,5,1,2].
        ("LC1", [3, 4, 5, 1, 2], [4, 1, 2], True),
        # Example 2: same root but subRoot = [4,1,2,None,None,None,0] is NOT.
        ("LC2", [3, 4, 5, 1, 2, None, None, None, None, 0],
         [4, 1, 2], False),

        # ---- Hand-built edge cases ----
        # Identical single-node trees.
        ("single-equal", [7], [7], True),
        # Single-node trees that differ.
        ("single-diff", [7], [9], False),
        # subRoot equals the entire root.
        ("subRoot==root", [1, 2, 3], [1, 2, 3], True),
        # subRoot is a deep leaf.
        ("deep-leaf-match", [1, 2, 3, 4, 5, 6, 7], [5], True),
        # Values match but structure differs: root has extra left child under
        # the "2"; subRoot is just [2, None, 3].
        ("values-match-shape-doesnt",
         [1, 2, 3, 4], [2, None, 3], False),
        # subRoot appears on the right branch.
        ("match-on-right", [1, 2, 3, None, None, 4, 5],
         [3, 4, 5], True),
        # Negative values (LC allows -10^4..10^4).
        ("negatives", [-1, -2, -3], [-2], True),
        # subRoot bigger than any subtree in root.
        ("subRoot-too-big", [1, 2], [1, 2, 3], False),
    ]

    failed = 0
    for name, root_vals, sub_vals, expected in cases:
        got = sol.isSubtree(_build(root_vals), _build(sub_vals))
        ok = (got == expected)
        flag = "PASS" if ok else "FAIL"
        if not ok:
            failed += 1
        print(f"  [{flag}] {name:<25} expected={expected!s:<5} got={got}")

    if failed == 0:
        print(f"\nAll tests passed. ({len(cases)} cases)")
    else:
        print(f"\n{failed}/{len(cases)} FAILED.")
