# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        queue = collections.deque()
        queue.append(root)
        res = []
        while queue:
            
            tmp = []
            for i in range(len(queue)):
                node = queue.popleft()
                tmp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(tmp)
        return res
                
        












# queue = deque()
# if not root:
#     return []
# res = []
# queue.append(root)
# curr = root;
# while queue:
#     res.append(curr.val)
#     if curr.left:
#         queue.append(curr.left)
#     if curr.right:
#         queue.append(curr.right)
#     curr = queue.popleft()
# return res

