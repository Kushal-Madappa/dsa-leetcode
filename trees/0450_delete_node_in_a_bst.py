# LeetCode: Delete Node in a BST (#450)
# https://leetcode.com/problems/delete-node-in-a-bst/
from typing import Optional


class Solution:
    def deleteNode(self, root: Optional["TreeNode"], key: int) -> Optional["TreeNode"]:
        if root is None:
            return None
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left
            succ = root.right
            while succ.left is not None:
                succ = succ.left
            root.val = succ.val
            root.right = self.deleteNode(root.right, succ.val)
        return root
