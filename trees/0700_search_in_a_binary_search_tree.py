# LeetCode: Search in a Binary Search Tree (#700)
# https://leetcode.com/problems/search-in-a-binary-search-tree/
from typing import Optional


class Solution:
    def searchBST(self, root: Optional["TreeNode"], val: int) -> Optional["TreeNode"]:
        while root and root.val != val:
            root = root.left if val < root.val else root.right
        return root
