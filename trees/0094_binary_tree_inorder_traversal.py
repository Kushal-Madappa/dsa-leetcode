# LeetCode: Binary Tree Inorder Traversal (#94)
# https://leetcode.com/problems/binary-tree-inorder-traversal/
from typing import List, Optional


class Solution:
    def inorderTraversal(self, root: Optional["TreeNode"]) -> List[int]:
        result = []
        stack = []
        node = root
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            result.append(node.val)
            node = node.right
        return result
