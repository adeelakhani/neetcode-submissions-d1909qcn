class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashSet = set()
        for num in nums:
            hashSet.add(num)
        length = 0
        biggestLength = 0
        for num in nums:
            if (num - 1) in hashSet:
                currNum = num -1
                while currNum not in hashSet:
                    length+=1
                    currNum+=1
                print(length)
                if length > biggestLength:
                    biggestLength = length
                length = 0
        return biggestLength