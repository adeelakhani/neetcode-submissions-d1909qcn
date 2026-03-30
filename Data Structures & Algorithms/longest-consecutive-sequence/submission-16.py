class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        print("hello world")
        allNums = set()
        for i in nums:
            allNums.add(i)
        base = 0
        longest = 0
        ovrlLongest = 0
        for num in nums:
            print(num)
            discovered = set()
            base = num
            if base not in discovered:
                while True:
                    if num-1 in allNums and num-1 not in discovered:
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