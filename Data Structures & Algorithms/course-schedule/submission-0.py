class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return False
        pTable = {i:[] for i in range(numCourses)}

        for prereq in prerequisites:
            pTable[prereq[0]].append(prereq[1])

        visited = set()
        def dfs(course):
            if course in visited: return False
            visited.add(course)

            prereqs = pTable[course]
            if len(prereqs) == 0:
                return True
            else:
                for prereq in prereqs:
                    value = dfs(prereq)
                    if value == False:
                        return False
                return True
        
        return dfs(0)