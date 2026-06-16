# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.valid = 0
        def dfs(root, max_=float('-inf')):
            if root == None:
                return
            if root.val >= max_:
                self.valid +=1
                max_ = root.val

            dfs(root.left, max_)
            dfs(root.right, max_)

        dfs(root)  
        return self.valid



