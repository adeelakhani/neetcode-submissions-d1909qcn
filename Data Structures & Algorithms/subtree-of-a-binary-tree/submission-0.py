# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
         
        def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]):
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val != q.val:
                return False
            left = isSameTree(p.left, q.left)
            right = isSameTree(p.right, q.right)
            return left and right
        def dfs(root):
            if isSameTree(root, subRoot):
                return True
            else:
                dfs(root.left)
                dfs(root.right)
            

        