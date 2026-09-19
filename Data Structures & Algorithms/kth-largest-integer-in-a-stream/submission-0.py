class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = nums # init min heap
        self.i = 0
        self.k = k
        heapq.heapify(self.heap)
        while len(self.heap) > k:
            heapq.heappop(self.heap)
        

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        while len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]
        # self.heap.append(val)
        # self.i+=1
        # # add the val
        # self.fixUp(self.heap, self.i-1)
        # smallest = 0
        # i = 0
        # f = self.k
        # while f > 0:
        #     smallest = self.heap[self.i]
        #     f-=1
        #     if 2*i + 1 < len(self.heap) and 2*i +2 < len(self.heap):
        #         if (self.heap[2*i + 2] < self.heap[2*i + 1]):
        #             i = 2*i + 2
        #         else:
        #             i = 2*i + 1
        #     elif 2*i+1 < len(self.heap):
        #         i = 2*i + 1
        # return smallest
    # def fixDown(self, heap, i):
    #     while 2*i + 1 < len(heap):
    #         # if right child, and right child less than left child, AND current node less
    #         # than right child
    #         if 2*i + 2 < len(heap) and (heap[2*i + 2] < heap[2*i + 1]) and heap[i] < heap[2*i + 2]:
    #             temp = heap[i]
    #             heap[i] = heap[2*i + 2]
    #             heap[2*i + 2] = temp
    #             i = 2*i + 2
    #         elif heap[i] < heap[2*i + 1]:
    #             temp = heap[i]
    #             heap[i] = heap[2*i + 1]
    #             heap[2*i + 1] = temp
    #             i = 2*i + 2
    #         else:
    #             break
    # def fixUp(self, heap, i):
    #     while heap[i] < heap[i//2]:
    #         temp = heap[i]
    #         heap[i] = heap[i//2]
    #         heap[i//2] = temp
    #         i = i//2 

        
