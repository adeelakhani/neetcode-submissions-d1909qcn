# from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # make the bucket sort the length of the list since that is the most amount of occurances
        # assume array is 6 nums long 
        freq = {} # dict to count occurances
        bucketsort = [[] for _ in range(0, len(nums)+1)] # 2d array which is 0 to 6 inner arrays

        for num in nums:
            freq[num] = freq.get(num, 0) + 1 # get occurances, key is num, value is the occurances
        for key in freq:
            bucketsort[freq[key]].append(key) # the index is the num of occurances,
                                              # and the value is the number itself
        # for num, cnt in count.items(): # could do it this way, for key, value in 
                                         # count.items(which is like (2, 3))
        #     bucketsort[cnt].append(num)  
        k_array = []
        for i in range(len(bucketsort)-1, -1, -1): # since the array is like 0 to 6, len is 7, so do 7 - 1
            for nums in bucketsort[i]: # go thru each inner bucket
                k_array.append(nums) # append each num, going backwards since its the MOST freq
                if len(k_array) == k: # if after appending a number, its k elements, we return the array
                    return k_array

            