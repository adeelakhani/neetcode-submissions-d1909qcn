class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total = sum(stones)
        goal = math.ceil(total/2)

        def memoization(i, remaining):
            if remaining <= 0 or i == len(stones):
                prog = goal - remaining
                otherside = total - prog
                return abs(prog - otherside)

            return min(memoization(i+1, remaining), memoization(i+1, remaining-stones[i]))

        return memoization(0, goal)