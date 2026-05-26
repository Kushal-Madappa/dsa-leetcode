"""
LeetCode 101. Symmetric Tree  (Easy)
https://leetcode.com/problems/symmetric-tree/

Given the root of a binary tree, return True iff the tree is a mirror of
itself (left subtree is the mirror reflection of the right subtree).

Approach -- the cross-pairing variant of #100
---------------------------------------------
This is the two-tree template from #100 with one knob flipped: where #100
descended on the *parallel* pairs (left, left) and (right, right), the
mirror check descends on the *crossed* pairs (left, right) and
(right, left). Same defensive base-case ordering, same recursion shape,
different pairing -- and that single change converts "are these trees
equal?" into "are these trees mirrors of each other?".

    mirror(a, b):
        if a is None and b is None: return True              # both empty -> mirror
        if a is None or  b is None: return False             # one empty  -> not mirror
        if a.val != b.val:          return False             # values must match
        return  mirror(a.left,  b.right)                     # crossed pair 1
            and mirror(a.right, b.left)                      # crossed pair 2

The outer call is `mirror(root.left, root.right)`. An empty tree is
vacuously symmetric, so we short-circuit `root is None` up top.

Why the base-case ordering matters (carried over from #100)
-----------------------------------------------------------
Tested in the order both-None -> one-None -> values, the recursion never
dereferences a None. Swap the order ("if a.val != b.val" first) and the
first time one side bottoms out you crash with AttributeError. This is
the same defensive ordering you'll reuse in every two-pointer / two-list
problem (merge sorted lists, intersection of lists, etc.).

Why the cross-pairing is the only thing that changes
----------------------------------------------------
Reading the recurrence side-by-side with #100 makes the symmetry obvious:

    #100 (same):    same(a.left,   b.left ) and same(a.right,  b.right)  # parallel
    #101 (mirror):  mirror(a.left, b.right) and mirror(a.right, b.left)   # crossed

That's the whole difference. File the cross-pairing knob alongside the
LOCAL_OK knob from #100 -- they're the two dials the two-tree template
exposes and most of the easy/medium two-tree problems can be solved by
turning one or both.

Edge cases
----------
- Empty tree (`root is None`)         -> True (vacuously symmetric).
- Single node                         -> True (no children -> both None).
- Left-only or right-only single child -> False (one side empty, the
                                           other not -- not a mirror).
- Same values but asymmetric *shape*  -> False. The "one-None" base case
                                          catches this; #101's first
                                          common bug is forgetting it
                                          and only comparing values.

Complexity
----------
n = number of nodes in the tree.
  Time  : O(n)         -- every node is visited once for an O(1) check.
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
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        def mirror(a: Optional[TreeNode], b: Optional[TreeNode]) -> bool:
            # Base cases in defensive order: both-None -> one-None -> values.
            if a is None and b is None:
                return True
            if a is None or b is None:
                return False
            if a.val != b.val:
                return False
            # Cross-pairing: outer-with-outer, inner-with-inner.
            return mirror(a.left, b.right) and mirror(a.right, b.left)

        return mirror(root.left, root.right)
# ----- END PASTE -----


# ---------------------------------------------------------------------------
# Local test harness -- stays on disk, NOT pasted into LeetCode.
# ---------------------------------------------------------------------------
def build(vals):
    """
    Build a tree from a level-order list with None for empty slots.
    Same helper used in 0100_same_tree.py / 0226_invert_binary_tree.py.
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


def run_tests():
    sol = Solution()
    cases = [
        # (input_vals,                                    expected, label)
        ([1, 2, 2, 3, 4, 4, 3],
         True,
         "LC sample 1 -- canonical symmetric 7-node tree"),
        ([1, 2, 2, None, 3, None, 3],
         False,
         "LC sample 2 -- same values, asymmetric shape"),
        ([],
         True,
         "edge -- empty tree is vacuously symmetric"),
        ([1],
         True,
         "edge -- single node"),
        ([1, 2],
         False,
         "edge -- only-left child, no mirror partner"),
        ([1, None, 2],
         False,
         "edge -- only-right child, no mirror partner"),
        ([1, 2, 2],
         True,
         "two children with equal vals, both leaves -> mirror"),
        ([1, 2, 2, 3, None, None, 3],
         True,
         "depth-3 symmetric, gaps mirrored"),
        ([1, 2, 2, 3, None, 3, None],
         False,
         "depth-3, gaps NOT mirrored (left has left, right has left too)"),
        ([1, 2, 2, 3, 4, 4, 5],
         False,
         "values asymmetric at deepest level (3 vs 5)"),
    ]

    all_pass = True
    for vals, expected, label in cases:
        root = build(vals)
        got = sol.isSymmetric(root)
        ok = got == expected
        all_pass = all_pass and ok
        print(f"[{'PASS' if ok else 'FAIL'}] {label}")
        if not ok:
            print(f"        got      : {got}")
            print(f"        expected : {expected}")

    print("All tests passed." if all_pass else "SOME TESTS FAILED.")


if __name__ == "__main__":
    run_tests()
