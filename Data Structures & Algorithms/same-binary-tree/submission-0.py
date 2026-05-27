# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        tree1 = []
        tree2 = []

        def dfs(node, arr):
            if not node:
                arr.append(None)
                return None

            arr.append(node.val)
            dfs(node.left, arr)
            dfs(node.right, arr)

        dfs(p, tree1)
        dfs(q, tree2)
        return tree1 == tree2