# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_ = 0
        dfs(root)
        return max_
        def dfs(root):
            if not root:
                return 0
            l = self.diameterOfBinaryTree(root.left)
            r = self.diameterOfBinaryTree(root.right)

            res = l + r
            max_ = max(res, max_)
        

