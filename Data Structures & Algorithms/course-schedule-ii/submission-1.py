class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {i: [] for i in range(numCourses)}

        for course, prereq in prerequisites:
            adj[course].append(prereq)
        # 0: [1]
        # 1: [0]
        # 2: [0]
        self.res = []
        visited = set()
        path = set()

        def dfs(course, visited, path):
            if course in path:
                self.res = []
                return False
            if course in visited:
                return
            visited.add(course)
            path.add(course)
            for prereq in adj[course]:
                if dfs(prereq, visited, path) == False:
                    return
            self.res.append(course)
            path.discard(course)

        for course in adj.keys():
            print(course)
            dfs(course, visited, path)
        
        return self.res