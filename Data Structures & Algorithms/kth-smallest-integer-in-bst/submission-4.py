# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k
        def dfs(root):
            if not root: return -1

            if self.k == 0:
                return root.val

            self.k -=1
            return dfs(root.left)
            return dfs(root.right)

        return dfs(root)













# stack = []
# curr = root
# while curr or stack:
#     if curr is None:
#         curr = stack.pop()
#         print(curr.val)
#         curr = curr.right
#     else:
#         stack.append(curr)
#         curr = curr.left
                
            
            
