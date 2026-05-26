"""
LeetCode 543. Diameter of Binary Tree  (Easy)
https://leetcode.com/problems/diameter-of-binary-tree/

Given the root of a binary tree, return the length of the *diameter* of the
tree -- the number of EDGES on the longest path between any two nodes in
the tree. The path may or may not pass through the root.

Approach -- the hybrid template (value + nonlocal mutation)
----------------------------------------------------------
This is the first problem in the trees track that needs BOTH halves of
the recursion toolkit at once:

  - From #104 (Maximum Depth): a helper that **returns** a value (height).
  - From #226 (Invert Binary Tree): a helper that **mutates** outer state.

The key insight: the longest path *through* a particular node is
    left_height + right_height
(measured in edges, with each child contributing its full height). The
diameter of the whole tree is the maximum of that quantity over every
node. So we run a single post-order DFS where each call:

  1. Recursively computes left/right *heights* (returned, like #104).
  2. Updates a running max diameter using `left + right` at this node
     (mutates outer state, like #226).
  3. Returns `1 + max(left, right)` so the parent can keep computing
     heights correctly.

That dual role -- "return one thing while quietly updating another" --
is the hybrid template, and almost every "longest/largest path in a
tree" problem fits it.

Why O(n) and why a single pass suffices
---------------------------------------
A naive approach is "for each node, compute left height + right height,
take the max" -- but each `height` call is O(n) in the worst case, so
that's O(n^2). The trick is that the post-order DFS *already* computes
every node's height once on the way back up; we just piggyback the
diameter update onto the return trip. Result: every node is visited
exactly once, and every node does O(1) work besides recursion. O(n).

The "edges vs. nodes" gotcha
----------------------------
The problem defines diameter as the number of *edges* on the path, not
nodes. A single-node tree therefore has diameter 0 (no edges), and a
two-node tree has diameter 1. The formula `left_height + right_height`
gives the right answer in edges *as long as* we define `height(None) =
0` (so a leaf node's two None children contribute 0 + 0 = 0 path
length through the leaf). If you mistakenly treat `height(None) = -1`
to "model the missing edge," you'll be off by 2 at every leaf.

The mental model that keeps this straight:
    height(node) = number of edges from `node` down to its deepest
                   descendant leaf (so height(leaf) = 0, height(None) = 0).
    path_through(node) = height(left) + height(right)
                         (each side is already in edges, and the two
                          edges from `node` to its children are
                          included as the "+1" each subtree's height
                          calculation added on its way back up).

Edge cases
----------
- Empty tree (`root is None`) -- diameter is 0 (no path, no edges).
- Single node -- diameter is 0.
- Two-node tree -- diameter is 1.
- Path-shaped tree of n nodes -- diameter is n-1 (every edge is in the
  longest path).
- "Diameter not through root" -- e.g., a balanced tree where two long
  paths meet in a deep internal node. The DFS catches this because the
  update happens at EVERY node, not just the root.

Complexity
----------
n = number of nodes.
  Time  : O(n)         -- one post-order traversal, O(1) work per node.
  Space : O(h)         -- recursion stack of depth = tree height.
                          Balanced: O(log n).  Skewed: O(n).
"""

from typing import Optional


# LeetCode provides this. Reproduced locally so the test harness runs.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# ----- PASTE INTO LEETCODE: from `class Solution:` down to end of method -----
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.best = 0  # running max diameter (in edges)

        def height(node: Optional[TreeNode]) -> int:
            # height(None) = 0 so a leaf has height 0 and the path length
            # through a leaf computes to 0 + 0 = 0 (correct: no edges).
            if node is None:
                return 0
            left = height(node.left)
            right = height(node.right)
            # Hybrid step: update the outer state on the way back up.
            # The longest path THROUGH this node has length left + right.
            if left + right > self.best:
                self.best = left + right
            # Return the standard "height" so the parent can keep going.
            return 1 + max(left, right)

        height(root)
        return self.best
# ----- END PASTE -----


# ---------------------------------------------------------------------------
# Local test harness -- stays on disk, NOT pasted into LeetCode.
# ---------------------------------------------------------------------------
def build(vals):
    """Build a tree from a level-order list with None for empty slots."""
    if not vals:
        return None
    it = iter(vals)
    root = TreeNode(next(it))
    queue = [root]
    for v in it:
        parent = queue[0]
        if not hasattr(parent, "_left_done"):
            parent._left_done = True
            if v is not None:
                parent.left = TreeNode(v)
                queue.append(parent.left)
        else:
            if v is not None:
                parent.right = TreeNode(v)
                queue.append(parent.right)
            queue.pop(0)
    return root


def run_tests():
    cases = [
        # (input_vals,                          expected, label)
        ([1, 2, 3, 4, 5],
         3,
         "LC sample 1 -- diameter 3 via 4 -> 2 -> 1 -> 3"),
        ([1, 2],
         1,
         "LC sample 2 -- single edge, diameter 1"),
        ([],
         0,
         "edge -- empty tree, diameter 0"),
        ([1],
         0,
         "edge -- single node, diameter 0"),
        ([1, 2, 3],
         2,
         "edge -- 3-node V shape, diameter 2"),
        ([1, 2, None, 3, None, 4, None, 5],
         4,
         "edge -- left-skewed 5-node chain, diameter 4"),
        ([1, None, 2, None, 3, None, 4, None, 5],
         4,
         "edge -- right-skewed 5-node chain, diameter 4"),
        ([1, 2, 3, 4, 5, 6, 7],
         4,
         "balanced 7-node tree: 4 -> 2 -> 1 -> 3 -> 7 (or symmetric)"),
        ([1, 2, 3, 4, None, None, 5, 6, None, None, 7],
         6,
         "diameter 6 via 6 -> 4 -> 2 -> 1 -> 3 -> 5 -> 7 (deep both sides)"),
    ]

    all_pass = True
    for vals, expected, label in cases:
        # Fresh Solution per case so `self.best` resets cleanly.
        sol = Solution()
        root = build(vals)
        got = sol.diameterOfBinaryTree(root)
        ok = got == expected
        all_pass = all_pass and ok
        print(f"[{'PASS' if ok else 'FAIL'}] {label}")
        if not ok:
            print(f"        got      : {got}")
            print(f"        expected : {expected}")

    print("All tests passed." if all_pass else "SOME TESTS FAILED.")


if __name__ == "__main__":
    run_tests()
