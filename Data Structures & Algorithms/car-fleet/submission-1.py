class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = sorted(zip(position, speed)) # o(nlogn) :((((
        # linear relationship: time to reach target
        # target = position + speed * time
        # so isolate for time, we get
        # time = (target - position)/speed
        times = []
        index = 0
        for pos,spd in pairs:
            times[index] = (target - pos)/spd
            index+=1
        clusters = []
        stack = []
        # if a time BEFORE is smaller than a time ahead then its part of that cluster
        for i in range(0, len(times)):
            tmp = []
            while stack and times[stack[-1]] < times[i]:
                tmp.append(times[stack[-1]])
                stack.pop()
            clusters.append(tmp)
            stack.append(times[i])
        return len(clusters)



            
        

