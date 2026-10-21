class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {i: [] for i in range(numCourses)}
        indegrees = [0]*numCourses
        for course, prereq in prerequisites:
            adj[prereq].append(course)
            indegrees[course]+=1


        queue = collections.deque()
        for course in range(len(indegrees)):
            if indegrees[course] == 0: queue.append(course)
        
        res = []
        while queue:
            course = queue.popleft()
            res.append(course)
            for neighbour in adj[course]:
                indegrees[neighbour] -= 1
                if indegrees[neighbour] == 0:
                    queue.append(neighbour)

        return res if sum(indegrees) == 0 else []














        
        
        # adj = {i: [] for i in range(numCourses)}

        # for course, prereq in prerequisites:
        #     adj[course].append(prereq)

        # self.res = []
        # visited = set()
        # path = set()

        # def dfs(course, visited, path):
        #     if course in path:
        #         return False
        #     if course in visited:
        #         return
        #     visited.add(course)
        #     path.add(course)
        #     for prereq in adj[course]:
        #         if dfs(prereq, visited, path) == False:
        #             return
        #     self.res.append(course)
        #     path.discard(course)

        # for course in adj.keys():
        #     if dfs(course, visited, path) == False:
        #         return []
            
        
        # return self.res