# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def dfs(root, P, Q):
            if not root:
                return
            
            if P.val < root.val and Q.val < root.val:
                return dfs(root.left, P, Q)
            elif P.val > root.val and Q.val > root.val:
                return dfs(root.right, P, Q)
            else:
                return root

        return dfs(root, p, q)
