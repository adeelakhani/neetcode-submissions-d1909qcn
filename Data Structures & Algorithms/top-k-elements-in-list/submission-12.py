from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        buckets = [[] for i in range(len(nums))]
        # [1,2,2,3,3,3]
        # [
            # [1], frequency 1, index 0
            # [2], frequency 2, index 1
            # [3], frequency 3
            # [], frequency 4
            # [], frequency 5
            # []  frequency 6
        # ]
        # k = 2
        for key,v in freq.items():
            buckets[v-1].append(key)
        
        print(buckets)
        res = []
        for i in range(len(buckets)-1,-1,-1):
            if len(buckets[i]) > 0 and len(res) < k:
                res.extend(buckets[i])
        return res

        
             