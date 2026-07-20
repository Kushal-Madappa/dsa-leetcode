# LeetCode: Average of Levels in Binary Tree (#637)
# https://leetcode.com/problems/average-of-levels-in-binary-tree/
from typing import List, Optional
from collections import deque


class Solution:
    def averageOfLevels(self, root: Optional['TreeNode']) -> List[float]:
        result: List[float] = []
        if root is None:
            return result
        q = deque([root])
        while q:
            size = len(q)
            total = 0
            for _ in range(size):
                node = q.popleft()
                total += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            result.append(total / size)
        return result
