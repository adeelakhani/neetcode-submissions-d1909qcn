class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = {i:[] for i in range(numCourses)}
        for course, prereq in prerequisites:
            adj[course].append(prereq)
        
        rel_prereqs = {i: () for i in range(numCourses)}
        def dfs(course, visited, path, target):
            if course in visited:
                return
            if course == target:
                return True
            visited.add(course)
            path.add(course)
            for neighbour in adj[course]:
                if dfs(neighbour, visited, path, target) == True:
                    return True
            return False
            path.discard(course)

        visited = set()
        path = set()
        res = []
        for start, target in queries:
            res.append(dfs(start, visited, path, target))
        return res