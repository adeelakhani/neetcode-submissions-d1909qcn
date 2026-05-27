# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_ = 0
        dfs(root)
        def dfs(root):
            if not root:
                return 0
            l = self.dfs(root.left)
            r = self.dfs(root.right)

            res = l + r
            self.max_ = max(res, max_)
        return max_
        
        

