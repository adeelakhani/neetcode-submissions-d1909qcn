class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        hashSet = set()
        for num in nums:
            hashSet.add(num)
        length = 0
        biggestLength = 0
        for num in nums:
            length = 1
            if (num - 1) in hashSet:
                currNum = num
                while currNum in hashSet:
                    length+=1
                    currNum+=1
            if length > biggestLength:
                biggestLength = length
            length = 0
        return biggestLength