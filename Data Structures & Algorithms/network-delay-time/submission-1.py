class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {}
        for i in range(1, n+1):
            adj[i] = []
        

        # d = destination, w = weight
        for s,d,w in times:
            adj[s].append( (d, w) )
        
        minheap = [(0, k)]
        res = {}
        while minheap:
            w1, n1 = heapq.heappop(minheap) # it is keyed by weight so w1 first
            # rmbr if its already in the result we have found the best result so we dont wanna add it.
            if n1 in res:  
                continue
            res[n1] = w1

            for n2, w2 in adj[n1]:
                if n2 not in res:
                    heapq.heappush(minheap, ((w1 + w2), n2))
        
        print(res)
        return max(res.values()) if len(res) == n else -1

