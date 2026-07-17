class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        consecutive = 0
        longestConsecutive = float('-inf')
        for i in nums:
            if i == 1:
                consecutive +=1
                longestConsecutive = max(longestConsecutive, consecutive)
            else:
                consecutive = 0
        return longestConsecutive