"""
LeetCode 110. Balanced Binary Tree  (Easy)
https://leetcode.com/problems/balanced-binary-tree/

Given the root of a binary tree, return True iff the tree is *height-
balanced* -- for every node, the heights of its left and right subtrees
differ by at most 1.

Approach -- the -1 sentinel trick (a value-returning DFS that signals failure)
-----------------------------------------------------------------------------
The naive approach is "for each node, compute left_height and
right_height, check |left - right| <= 1, recurse into children." That's
O(n^2) because every node triggers a height calculation that walks its
whole subtree.

Better: do a single post-order DFS that returns the height of the
current subtree, BUT returns a sentinel `-1` the moment any imbalance
is detected. Once a subtree reports -1, every ancestor short-circuits
and also returns -1, so the answer is "is the root's height != -1?"

  def height(node):
      if node is None: return 0
      L = height(node.left)
      if L == -1: return -1                  # short-circuit up
      R = height(node.right)
      if R == -1: return -1                  # short-circuit up
      if abs(L - R) > 1: return -1           # this node is the imbalance
      return 1 + max(L, R)

This is the bridge between #104 (height as a value) and the hybrid
template from #543 (height + outer mutation). Here we don't mutate
outer state; we *overload the return value* with a "failure" signal.
Same effect, slightly different lever -- and it's a pattern you'll see
again in BST validation (#98), where the return is "(is_bst, min, max)"
or a sentinel, and in #1325 (delete leaves), where the return is the
subtree itself or None.

Why -1 is a safe sentinel here
-------------------------------
Heights of real subtrees are non-negative integers (0 for None, 0 for a
leaf, etc.). The value -1 cannot be produced by any valid subtree, so
seeing it unambiguously means "we already proved unbalance somewhere
below." If the problem's value domain *could* include -1 (e.g., heights
that might naturally be -1), you'd need a separate flag instead.

Why the single-pass version is O(n)
-----------------------------------
Each node is visited at most once. The "short-circuit" returns make the
worst case faster, not slower -- they only ever skip work. So total
work is bounded by 1 * n = O(n), versus the naive O(n^2).

Edge cases
----------
- Empty tree (`root is None`)            -> True (vacuously balanced).
- Single node                            -> True (heights of children
                                            are 0 and 0).
- Perfectly skewed chain of n nodes      -> False for n >= 3 (heights
                                            differ by n-1 at the top).
- A tree where ONE deep subtree is
  unbalanced but the root looks balanced -> False. The recursion catches
                                            this because the sentinel
                                            propagates from wherever
                                            the imbalance lives.

Complexity
----------
n = number of nodes.
  Time  : O(n)         -- one post-order traversal, O(1) per node.
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
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(node: Optional[TreeNode]) -> int:
            # Returns the subtree's height, or -1 if any imbalance was
            # detected anywhere in this subtree.
            if node is None:
                return 0
            left = height(node.left)
            if left == -1:
                return -1
            right = height(node.right)
            if right == -1:
                return -1
            if abs(left - right) > 1:
                return -1
            return 1 + max(left, right)

        return height(root) != -1
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
    sol = Solution()
    cases = [
        # (input_vals,                                    expected, label)
        ([3, 9, 20, None, None, 15, 7],
         True,
         "LC sample 1 -- balanced 5-node tree"),
        ([1, 2, 2, 3, 3, None, None, 4, 4],
         False,
         "LC sample 2 -- depth-4 left subtree, depth-1 right -> unbalanced"),
        ([],
         True,
         "edge -- empty tree is vacuously balanced"),
        ([1],
         True,
         "edge -- single node is balanced"),
        ([1, 2],
         True,
         "two nodes -- heights 1 and 0, diff = 1, balanced"),
        ([1, 2, None, 3],
         False,
         "left-skewed chain of 3 -- root sees heights 2 and 0, unbalanced"),
        ([1, 2, 3, 4, 5, 6, 7],
         True,
         "complete binary tree of 7 nodes -- balanced"),
        ([1, None, 2, None, 3],
         False,
         "right-skewed chain -- root sees heights 0 and 2"),
        ([1, 2, 3, 4, 5, None, None, 6, None, None, None, 7],
         False,
         "deep left subtree height vs short right -- unbalanced via sentinel"),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
         True,
         "complete binary tree of 15 nodes -- balanced"),
    ]

    all_pass = True
    for vals, expected, label in cases:
        root = build(vals)
        got = sol.isBalanced(root)
        ok = got == expected
        all_pass = all_pass and ok
        print(f"[{'PASS' if ok else 'FAIL'}] {label}")
        if not ok:
            print(f"        got      : {got}")
            print(f"        expected : {expected}")

    print("All tests passed." if all_pass else "SOME TESTS FAILED.")


if __name__ == "__main__":
    run_tests()
