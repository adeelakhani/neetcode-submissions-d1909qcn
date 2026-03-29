from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        buckets = [ [] for i in range(0,len(nums)+1) ]
        for i in nums:
            freq[i] = freq.get(i, 0) + 1
        # at most a number can occur len(nums) times, so the array is 0 to nums size
        for key in freq:
            buckets[ freq[key] ].append(key)
        # now we have some "buckets" in which the buckets at a far index are                                           
        # go through the buckets backwards, and stop going through them(check each pass) if they are
        # at a length of "k"
        answer = []
        for i in range(len(nums), -1, -1):
            for j in buckets[i]:
                answer.append(j)
                if len(answer) == k:
                    return answer
        
        
             