# LeetCode: Binary Tree Level Order Traversal (#102)
# https://leetcode.com/problems/binary-tree-level-order-traversal/
from typing import List, Optional
from collections import deque


class Solution:
    def levelOrder(self, root: Optional["TreeNode"]) -> List[List[int]]:
        if not root:
            return []
        result: List[List[int]] = []
        q = deque([root])
        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            result.append(level)
        return result
