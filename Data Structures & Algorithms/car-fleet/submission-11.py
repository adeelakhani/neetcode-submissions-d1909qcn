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
        # so go from the right then look for everything 
        # smaller than it until somehting is bigger
        # so in this case: [2, 1, 2, 3, 2], we have 2 fleets:
        # [2, 1, 2, 3] and [2]
        for i in range(len(times) - 1, -1, -1):
            if not stack or times[i] > stack[-1]:
                stack.append(times[i])

        return len(stack)


