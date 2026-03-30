class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        i = 0
        for num, i in enumerate(nums):
            value = target - num
            if value in hashmap:
                return [hashmap[value], i]
            hashmap[num] = i 