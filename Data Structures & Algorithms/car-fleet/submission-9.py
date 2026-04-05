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

        for time in times:
            if not stack or time > stack[-1]:
                stack.append(time)

        return len(stack)


