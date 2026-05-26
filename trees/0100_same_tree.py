"""
LeetCode 100. Same Tree  (Easy)
https://leetcode.com/problems/same-tree/

Given the roots of two binary trees `p` and `q`, return True iff the two
trees are *structurally identical AND every corresponding pair of nodes
has the same value*.

Approach — parallel recursion on two trees
------------------------------------------
A direct extension of the tree-recursion template installed by #104.
The recursion compares two nodes at a time, descending in lockstep.

Base cases (in this order — the order matters):
  1. Both None         -> True   (two empty subtrees ARE the same)
  2. Exactly one None  -> False  (different structure)
  3. Values differ     -> False  (same shape so far, but mismatched node)

Recursive step:
  Both subtrees must agree:
     isSameTree(p.left, q.left)  AND  isSameTree(p.right, q.right)

Why "both None first" is important:
  If we tested `p.val != q.val` first we'd crash with AttributeError when
  one of them is None. The ordering `both-None -> one-None -> values`
  short-circuits cleanly without ever dereferencing a None.

Complexity
----------
n = total number of nodes visited (bounded by min(|p|, |q|) in the worst
mismatch, and by max in the all-equal case).
  Time  : O(n)         — every visited node is constant work.
  Space : O(h)         — recursion stack of depth = tree height.
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
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        if p.val != q.val:
            return False
        return (
            self.isSameTree(p.left,  q.left)
            and
            self.isSameTree(p.right, q.right)
        )
# ----- END PASTE -----


# ---------------------------------------------------------------------------
# Local test harness — stays on disk, NOT pasted into LeetCode.
# ---------------------------------------------------------------------------
def build(vals):
    """
    Build a tree from a level-order list with None for empty slots.
    Example: [1, 2, 3]            ->    1
                                       / \
                                      2   3
             [1, 2, None, 3]       ->    1
                                        /
                                       2
                                      /
                                     3
    """
    if not vals:
        return None
    it = iter(vals)
    root = TreeNode(next(it))
    queue = [root]
    for v in it:
        parent = queue[0]
        # try left first
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
        # (p_vals,            q_vals,            expected, label)
        ([1, 2, 3],           [1, 2, 3],         True,  "LC sample 1 — identical 3-node tree"),
        ([1, 2],              [1, None, 2],      False, "LC sample 2 — same vals, mirrored structure"),
        ([1, 2, 1],           [1, 1, 2],         False, "LC sample 3 — same shape, wrong values"),
        ([],                  [],                True,  "edge — both empty"),
        ([1],                 [],                False, "edge — single node vs empty"),
        ([],                  [0],               False, "edge — empty vs zero-node (value matters too)"),
        ([1, 2, 3, 4, 5],     [1, 2, 3, 4, 5],   True,  "edge — perfect-ish small tree, identical"),
        ([1, 2, 3, 4, 5],     [1, 2, 3, 4, 6],   False, "edge — single deep-leaf mismatch"),
        ([5, 4, 8, 11, None, 17, 4, 7, 2, None, None, 5, 1],
         [5, 4, 8, 11, None, 17, 4, 7, 2, None, None, 5, 1],
         True,
         "deep tree — identical, exercises full recursion"),
        ([5, 4, 8, 11, None, 17, 4, 7, 2, None, None, 5, 1],
         [5, 4, 8, 11, None, 17, 4, 7, 2, None, None, 5, 2],
         False,
         "deep tree — last leaf differs"),
    ]

    all_pass = True
    for p_vals, q_vals, expected, label in cases:
        p = build(p_vals)
        q = build(q_vals)
        got = sol.isSameTree(p, q)
        ok = got == expected
        all_pass = all_pass and ok
        print(f"[{'PASS' if ok else 'FAIL'}] {label}: got {got}, want {expected}")

    print("All tests passed." if all_pass else "SOME TESTS FAILED.")


if __name__ == "__main__":
    run_tests()
