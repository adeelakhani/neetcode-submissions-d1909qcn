# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.isCooked = False
        def dfs(root):
            if not root:
                return 0

            heightLeft = dfs(root.left)
            heightRight = dfs(root.right)
            if abs(heightLeft - heightRight) > 1:
                self.isCooked = True
            height = 0
            if heightLeft > heightRight:
                height = heightLeft
            else:
                height = heightRight
            
            return 1 + height

            
        dfs(root)
        if not self.isCooked:
            return True
        else:
            return False
        

        