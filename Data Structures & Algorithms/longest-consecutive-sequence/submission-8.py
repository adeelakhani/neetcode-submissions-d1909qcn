class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums.length() == 1:
            return 1
        hashSet = set()
        for num in nums:
            hashSet.add(num)
        length = 0
        biggestLength = 0
        for num in nums:
            if (num - 1) in hashSet:
                currNum = num -1
                while currNum in hashSet:
                    length+=1
                    currNum+=1
                if length > biggestLength:
                    biggestLength = length
                length = 0
        return biggestLength