class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        i = 0
        #{5:0, 6:1}
        for i, num in enumerate(nums): # index, value
            value = target - num
            if value in hashmap: # if index in hashmap always is o(1), value in hashmap is o(n)
                return [hashmap[value], i]
            hashmap[num] = i 