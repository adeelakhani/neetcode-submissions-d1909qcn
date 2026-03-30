class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        allNums = set()
        for i in nums:
            allNums.add(i)
        base = 0
        ovrlLongest = 0
        discovered = set()
        for num in nums:
            print(num)
            longest=0
            base = num
            if base not in discovered:
                while True:
                    print(num)
                    if base-1 in allNums and base-1 not in discovered:
                        base = num-1
                    else:
                        discovered.add(base)
                        longest +=1
                        if base+1 in allNums:
                            base = base+1
                        else:
                            break
                if longest > ovrlLongest:
                    ovrlLongest = longest
        return ovrlLongest