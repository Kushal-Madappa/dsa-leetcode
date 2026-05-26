"""
LeetCode 104 -- Maximum Depth of Binary Tree   (Easy)
=====================================================

Topic tags : Tree, Depth-First Search, Breadth-First Search, Binary Tree,
             Recursion.

Problem
-------
Given the root of a binary tree, return its maximum depth.  A binary tree's
maximum depth is the number of nodes along the longest path from the root
node down to the farthest leaf node.

Approach -- straight recursion
------------------------------
The depth of an empty tree is 0.  The depth of a non-empty tree is one more
than the maximum depth of its two children:

    depth(None) = 0
    depth(node) = 1 + max(depth(node.left), depth(node.right))

That's it.  Each node is visited exactly once and contributes O(1) work.

Why this is the canonical "hello world" of tree recursion
---------------------------------------------------------
Every tree-recursion pattern installs three reflexes:
  1. **Base case at the empty subtree** (`None`), not at the leaf.  Returning
     from `None` is what makes the leaf's recursive call collapse cleanly to
     `1 + max(0, 0) = 1`.  Special-casing leaves is a beginner's trap.
  2. **The recursive call is a value, not a side effect.**  `depth(node.left)`
     *returns* the depth of the left subtree.  Tree problems get easy once
     you stop trying to thread mutable state and just trust the return.
  3. **One line of "combine."**  After the two recursive calls return, the
     local work is a single arithmetic combine (`1 + max(...)`).  This is
     the shape of almost every tree-recursion problem: recurse left, recurse
     right, combine, return.

Complexity
----------
  Time  : O(N)   -- one visit per node.
  Space : O(H)   -- recursion stack, H = tree height.
                    Balanced: O(log N).  Skewed: O(N).

Submission note
---------------
Copy ONLY the `class Solution` block into LeetCode.  The `TreeNode` class
and `Optional` import are provided by LeetCode's environment.  The
`TreeNode` stub and the test harness below are local-only.
"""

from typing import Optional, List


# Local TreeNode stub -- LeetCode provides this; do NOT paste into LeetCode.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# ===================== PASTE THIS BLOCK INTO LEETCODE =====================
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
# =================== END LEETCODE SUBMISSION BLOCK ========================


# ---------------- local test harness ----------------
def _build(values: List):
    """Build a tree from LeetCode's level-order list (None = missing)."""
    if not values:
        return None
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    while queue and i < len(values):
        node = queue.pop(0)
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root


if __name__ == "__main__":
    s = Solution()
    cases = [
        # LeetCode official samples
        ([3, 9, 20, None, None, 15, 7], 3),
        ([1, None, 2],                  2),
        # Hand-built edges
        ([],                            0),   # empty tree
        ([1],                           1),   # single node
        ([1, 2, 3, 4, 5, 6, 7],         3),   # perfect tree of depth 3
        ([1, 2, None, 3, None, 4],      4),   # left-skewed chain
        ([1, None, 2, None, 3, None, 4],4),   # right-skewed chain
    ]
    for vals, expected in cases:
        got = s.maxDepth(_build(vals))
        assert got == expected, f"FAIL {vals!r}: got {got}, want {expected}"
    print("All tests passed.")
