class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for i, n in enumerate(nums):
            toLook = target - n
            if toLook in hashMap:
                return [hashMap[toLook], i]
            hashMap[n] = i
