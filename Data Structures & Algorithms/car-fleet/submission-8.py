class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = sorted(zip(position, speed)) # o(nlogn) :((((
        # linear relationship: time to reach target
        # target = position + speed * time
        # so isolate for time, we get
        # time = (target - position)/speed
        times = []
        for pos,spd in pairs:
            times.append((target - pos)/spd)

        stack = []
        # if a time BEFORE is smaller than a time ahead then its part of that cluster
        for i in range(0, len(times)):
            while stack and stack[-1] < times[i]:
                stack.pop()
            stack.append(times[i])
        return len(stack)


