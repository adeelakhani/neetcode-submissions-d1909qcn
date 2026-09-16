# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        stack = []

        def backtrack(root):
            if not root:
                return
            stack.append(root.val)
            if not root.left and not root.right:
                if sum(stack) == targetSum:
                    return True
            if backtrack(root.left):
                return True
            if backtrack(root.right):
                return True
            stack.pop()
            return False

        return backtrack(root)

        
        
