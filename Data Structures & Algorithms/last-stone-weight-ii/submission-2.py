class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total = sum(stones)
        goal = math.ceil(total/2)

        cache = {}
        def memoization(i, remaining):

            if (i, remaining) in cache:
                return cache[(i, remaining)]

            if remaining <= 0 or i == len(stones):
                prog = goal - remaining
                otherside = total - prog
                return abs(prog - otherside)

            cache[(i, remaining)] = min(memoization(i+1, remaining), memoization(i+1, remaining-stones[i]))
            return cache[(i, remaining)]

        return memoization(0, goal)