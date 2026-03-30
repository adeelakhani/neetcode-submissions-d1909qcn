class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashSet = set()
        for num in nums:
            hashSet.add(num)
        length = 0
        for num in nums:
            if (num - 1) in hashSet:
                length+=1
        return length