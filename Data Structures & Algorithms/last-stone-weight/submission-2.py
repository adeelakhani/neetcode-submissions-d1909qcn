class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-i for i in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            print(stones)
            y = heapq.heappop(stones)
            print(y)
            x = heapq.heappop(stones)
            if x > y:
                heapq.heappush(stones, y-x)
        return 0 if not stones else -1*stones[0]