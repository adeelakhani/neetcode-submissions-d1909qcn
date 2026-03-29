class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(0, len(nums)):
            hashmap[nums[i]] = i
        for i in range(0, len(nums)):
            diff = target-nums[i]
            if diff in hashmap and hashmap[diff] != i:
                return [i, hashmap[diff]]
        return [0,100]