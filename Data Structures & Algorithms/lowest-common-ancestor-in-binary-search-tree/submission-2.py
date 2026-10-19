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
                return None
            if P.val >= root.val and Q.val < root.val or Q.val >= root.val and P.val:
                return root
            return dfs(root.left, P, Q) if dfs(root.left, P, Q) else dfs(root.right, P, Q)
        

        return dfs(root,p,q)
