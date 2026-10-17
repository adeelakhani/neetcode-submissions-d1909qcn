class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        
        res = {}
        adj = [[] for i in range(n)]
        probIndex = 0
        for start, end in edges:
            adj[start].append((end, succProb[probIndex]))
            adj[end].append((start, succProb[probIndex]))
            probIndex+=1
        # adj[0] = [(1, 0.5), (2, 0.2)] 
        # adj[1] = [0, 2]
        # adj[2] = [1, 0]


        # res = {
            # 0: -1
            # 
        # }
        maxheap = [(-1, start_node)]
        while maxheap:
            w1, n1 = heapq.heappop(maxheap)
            if n1 in res:
                continue
            res[n1] = w1
            for dest, prob in adj[n1]:
                if dest not in res:
                    heapq.heappush(maxheap, (prob * w1, dest) )
        
        return -1 * res[end_node] if end_node in res else 0
