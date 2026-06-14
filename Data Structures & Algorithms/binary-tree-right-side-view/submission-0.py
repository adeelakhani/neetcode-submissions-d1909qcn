# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # go thru level by level and only include the right most in each level
        # works easily cus the queue that will hold the shit 
        if not root:
            return []
        queue = deque()
        queue.append(root)
        res = []
        while queue:
            level = len(queue)
            for i in range(0, level):
                curr = queue.popleft()
                if curr.left: queue.append(curr.left)
                if curr.right: queue.append(curr.right)
                if i == level-1:
                    res.append(curr.val)
        return res
