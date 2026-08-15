# LeetCode: Lowest Common Ancestor of a Binary Search Tree (#235)
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/


class Solution:
    def lowestCommonAncestor(self, root: "TreeNode", p: "TreeNode", q: "TreeNode") -> "TreeNode":
        node = root
        while node:
            if p.val < node.val and q.val < node.val:
                node = node.left
            elif p.val > node.val and q.val > node.val:
                node = node.right
            else:
                return node
