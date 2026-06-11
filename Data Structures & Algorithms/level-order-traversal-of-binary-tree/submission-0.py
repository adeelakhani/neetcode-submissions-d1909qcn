# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque()
        queue.append(root)
        ans = []
        while queue:
            level = []
            inThisLevel = len(queue) # get length BEFORE hand. THEN we go through all the ones on this level
                                     #  and add the children
            for i in range(0, inThisLevel):
                curr = queue.popleft()
                level.append(curr.val)
                if curr.left: queue.append(curr.left)
                if curr.right: queue.append(curr.right)
            ans.append(level)
        return ans












# queue = deque()
# if not root:
#     return []
# res = []
# queue.append(root)
# curr = root;
# while queue:
#     res.append(curr.val)
#     if curr.left:
#         queue.append(curr.left)
#     if curr.right:
#         queue.append(curr.right)
#     curr = queue.popleft()
# return res

