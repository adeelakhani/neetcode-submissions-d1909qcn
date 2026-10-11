"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        visited = {}

        def dfs(node, copyNode, visited):
            if node in visited:
                return
            
            visited[node] = copyNode

            for neighbor in node.neighbors:
                if neighbor in visited:
                    newNeighbor = visited[neighbor]
                else:
                    newNeighbor = Node(neighbor.val)
                copyNode.neighbors.append(newNeighbor)
                dfs(neighbor, newNeighbor, visited)
        
        clone = Node(node.val)
        dfs(node, clone, visited)
        return clone