class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {i:[] for i in range(numCourses)}
        for course, preq in prerequisites:
            adj[course].append(preq)
        



        def dfs(node, visited, path):
            if node in path:
                return False
            if node in visited:
                return
            visited.add(node)
            path.add(node)

            for neighbour in adj[node]:
                res = dfs(neighbour, visited, path)
                if res == False:
                    return False
            path.discard(node)
            return True
        

        visited = set()
        path = set()
        for node in adj.keys():
            res = dfs(node, visited, path)
            if res == False:
                return res
        return True
