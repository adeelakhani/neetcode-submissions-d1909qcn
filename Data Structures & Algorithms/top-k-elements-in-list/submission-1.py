# from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # make the bucket sort the length of the list since that is the most amount of occurances
        # something can have
        freq = {}
        bucketsort = [[] for _ in range(0, len(nums)+1)]

        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        for key in freq:
            bucketsort[freq[key]].append(key) 
        k_array = []
        for i in range(len(bucketsort), -1, -1):
            for nums in bucketsort[i]:
                k_array.append(nums)
                if len(k_array) == k:
                    return k_array

            