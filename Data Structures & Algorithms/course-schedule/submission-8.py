class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pTable = {i:[] for i in range(numCourses)}

        for prereq in prerequisites:
            pTable[prereq[0]].append(prereq[1])
        print(pTable)
        visited = set()
        def dfs(course):
            if course in visited: return False

            prereqs = pTable[course]
            if len(prereqs) == 0:
                return True
            visited.add(course)
            for prereq in prereqs:
                if not dfs(prereq):
                    return False
            visited.remove(course)
            pTable[course] = []
            return True
        
        for key,value in pTable.items():
            if not dfs(key):
                return False
        return True
