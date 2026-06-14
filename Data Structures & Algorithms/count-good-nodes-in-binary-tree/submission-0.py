# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return []

        queue = deque()
        queue.append(root)
        res = 1
        rootVal = root.val
        while queue:
            level = len(queue)
            for i in range(0, level):
                curr = queue.popleft()
                if curr.left:
                    queue.append(curr.left)
                    if curr.left.val >= rootVal:
                        res+=1
                if curr.right:
                    queue.append(curr.right)
                    if curr.right.val >= rootVal:
                        res+=1
        return res



