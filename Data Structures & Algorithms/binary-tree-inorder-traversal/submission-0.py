# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.inOrder = []
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            self.inOrder.append(root.val)
            print(self.inOrder)
            dfs(root.right)
        dfs(root)
        return self.inOrder