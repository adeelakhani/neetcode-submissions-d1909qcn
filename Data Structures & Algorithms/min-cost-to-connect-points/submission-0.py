class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # prims wants the total of everythig in the res to be the lowest

        adj = {i:[] for i in range(0, len(points))}
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                adj[i].append([j, self.calculateDistance(points[i], points[j])])
                adj[j].append([i, self.calculateDistance(points[i], points[j])])
        
        res = 0
        visited = set()
        minHeap = [(0, 0)]

        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in visited:
                continue
            visited.add(n1)
            res +=w1

            for n2,w2 in adj[n1]:
                if n2 not in visited:
                    heapq.heappush(minHeap, (w2, n2))
        
        return res
    
    def calculateDistance(self, point1, point2):
        p1x, p1y = point1
        p2x, p2y = point2
        return abs(p1x - p2x) + abs(p1y - p2y)
        