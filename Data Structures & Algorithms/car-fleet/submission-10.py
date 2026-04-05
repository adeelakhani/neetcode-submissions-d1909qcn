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

        for i in range(len(times) - 1, -1, -1):
            if not stack or times[i] > stack[-1]:
                stack.append(times[i])

        return len(stack)


