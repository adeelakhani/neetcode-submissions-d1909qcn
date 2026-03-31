class MinStack:
    def __init__(self):
        self.minimum = float('inf')
        self.stack = []
        self.minTrack = []
    def push(self, val: int) -> None:
        self.stack.append(val)
        if val < self.minimum:
            self.minimum = val
        self.minTrack.append(self.minimum)

    def pop(self) -> None:
        self.stack.pop()
        self.minTrack.pop()
        if self.minTrack:
            self.minimum = self.minTrack[-1]
        else:
            self.minimum = float('inf')

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minTrack[-1]
        
