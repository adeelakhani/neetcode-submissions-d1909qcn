class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        i = 0
        #{5:0, 6:1}
        for i, num in enumerate(nums):
            value = target - num
            if value in hashmap:
                return [hashmap[value], i]
            hashmap[num] = i 