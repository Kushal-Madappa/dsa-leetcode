# LeetCode: Binary Tree Right Side View (#199)
# https://leetcode.com/problems/binary-tree-right-side-view/
from typing import Optional, List
from collections import deque


class Solution:
    def rightSideView(self, root: Optional['TreeNode']) -> List[int]:
        if not root:
            return []
        result = []
        q = deque([root])
        while q:
            size = len(q)
            for i in range(size):
                node = q.popleft()
                if i == size - 1:
                    result.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return result
