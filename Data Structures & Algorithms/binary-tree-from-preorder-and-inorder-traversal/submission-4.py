# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right

# class Solution:
#     def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
#         if not preorder or not inorder:
#             return None
#         root = TreeNode(preorder[0])
#         index = inorder.index(preorder[0])
#         root.left = self.buildTree(preorder[1:index+1], inorder[:index])
#         root.right = self.buildTree(preorder[index+1:], inorder[index+1:])
#         return root

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        # value -> index in inorder
        inorderIndex = {}
        for i, val in enumerate(inorder):
            inorderIndex[val] = i

        preIndex = 0

        def dfs(left, right):
            nonlocal preIndex

            # No nodes in this subtree
            if left > right:
                return None

            # Root is always next in preorder
            rootVal = preorder[preIndex]
            preIndex += 1

            root = TreeNode(rootVal)

            # Split inorder into left/right subtrees
            mid = inorderIndex[rootVal]

            root.left = dfs(left, mid - 1)
            root.right = dfs(mid + 1, right)

            return root

        return dfs(0, len(inorder) - 1)