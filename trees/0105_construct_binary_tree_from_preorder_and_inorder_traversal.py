# LeetCode: Construct Binary Tree from Preorder and Inorder Traversal (#105)
# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
from typing import List, Optional


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        idx = {v: i for i, v in enumerate(inorder)}
        self.pre_i = 0

        def build(l: int, r: int) -> Optional[TreeNode]:
            if l > r:
                return None
            val = preorder[self.pre_i]
            self.pre_i += 1
            node = TreeNode(val)
            m = idx[val]
            node.left = build(l, m - 1)
            node.right = build(m + 1, r)
            return node

        return build(0, len(inorder) - 1)
