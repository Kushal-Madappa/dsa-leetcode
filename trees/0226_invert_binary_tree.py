"""
LeetCode 226. Invert Binary Tree  (Easy)
https://leetcode.com/problems/invert-binary-tree/

Given the root of a binary tree, invert the tree (mirror it left/right at
every node) and return the new root.

Approach -- single-tree recursion with a side effect
----------------------------------------------------
This is the *mutating* cousin of #104. Where #104 returned a computed
value (depth) at every level, this problem mutates the node itself.
The whole solution is three lines of body:

    invert(None) = None                                # base case
    swap(node.left, node.right)                        # local side effect
    invert(node.left); invert(node.right)              # recurse into the
                                                       # *new* children
    return node

Why "swap THEN recurse" (or equivalently, "recurse THEN return") both work
--------------------------------------------------------------------------
The swap is purely structural -- it touches the two child *pointers* on
`node` and never reads or writes the deeper subtrees. So whether the
recursion happens before or after the swap doesn't change the final tree;
each call is responsible only for the swap at its own node. The version
below swaps first, recurses second, which reads most naturally as "I'm
the manager -- I swap my own kids, then delegate the rest."

Return-value vs side-effect tree recursion
------------------------------------------
The template installed by #104 was: "every recursive call returns a
value, the parent combines child values." Today's template is: "every
recursive call mutates its node and returns the (same) node so callers
can chain." Spotting which template a problem wants is the single most
useful tree-recursion reflex -- you'll see the same split again in #543
(Diameter -- both: compute a value AND track a global max via mutation)
and #114 (Flatten Binary Tree -- pure mutation).

Edge cases
----------
- Empty tree (`root is None`) -> return None. The recursion's base case
  handles this without any caller-side `if`.
- Single node -> swap of two `None` children is a no-op; the node is
  returned unchanged.
- Already-mirrored tree -> inverts back to the original shape. (Inversion
  is its own inverse.)

Complexity
----------
n = number of nodes in the tree.
  Time  : O(n)         -- each node is visited exactly once for an O(1) swap.
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
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        # Swap the two child pointers at THIS node...
        root.left, root.right = root.right, root.left
        # ...then let each subtree invert itself.
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
# ----- END PASTE -----


# ---------------------------------------------------------------------------
# Local test harness -- stays on disk, NOT pasted into LeetCode.
# ---------------------------------------------------------------------------
def build(vals):
    """
    Build a tree from a level-order list with None for empty slots.
    Mirrors the helper used by 0100_same_tree.py.
    """
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


def to_level_order(root):
    """
    Serialize a tree back to a level-order list with None for empty slots.
    Trailing Nones are trimmed so [1, 2, 3, None, None] becomes [1, 2, 3].
    """
    if root is None:
        return []
    out = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node is None:
            out.append(None)
        else:
            out.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
    while out and out[-1] is None:
        out.pop()
    return out


def run_tests():
    sol = Solution()
    cases = [
        # (input_vals,                              expected_inverted_level_order, label)
        ([4, 2, 7, 1, 3, 6, 9],
         [4, 7, 2, 9, 6, 3, 1],
         "LC sample 1 -- balanced 7-node tree"),
        ([2, 1, 3],
         [2, 3, 1],
         "LC sample 2 -- 3-node tree"),
        ([],
         [],
         "LC sample 3 -- empty tree"),
        ([1],
         [1],
         "edge -- single node, swap of two Nones is a no-op"),
        ([1, 2],
         [1, None, 2],
         "edge -- only-left becomes only-right"),
        ([1, None, 2],
         [1, 2],
         "edge -- only-right becomes only-left"),
        ([1, 2, 3, 4, None, None, 5],
         [1, 3, 2, 5, None, None, 4],
         "asymmetric 5-node tree -- deep leaves on both sides"),
    ]

    all_pass = True
    for vals, expected, label in cases:
        root = build(vals)
        got_root = sol.invertTree(root)
        got = to_level_order(got_root)
        ok = got == expected
        all_pass = all_pass and ok
        print(f"[{'PASS' if ok else 'FAIL'}] {label}")
        if not ok:
            print(f"        got      : {got}")
            print(f"        expected : {expected}")

    # Inversion is its own inverse -- double-invert should give back the input.
    double_invert_cases = [
        [4, 2, 7, 1, 3, 6, 9],
        [1, 2, 3, 4, 5, 6, 7],
        [5, 4, 8, 11, None, 17, 4, 7, 2, None, None, 5, 1],
    ]
    for vals in double_invert_cases:
        root = build(vals)
        once = sol.invertTree(root)
        twice = sol.invertTree(once)
        got = to_level_order(twice)
        ok = got == vals
        all_pass = all_pass and ok
        print(f"[{'PASS' if ok else 'FAIL'}] double-invert restores: {vals}")

    print("All tests passed." if all_pass else "SOME TESTS FAILED.")


if __name__ == "__main__":
    run_tests()
