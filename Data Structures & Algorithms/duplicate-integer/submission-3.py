class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        soFar = set()
        for i in nums:
            if i in soFar:
                return True
            else:
                soFar.add(i)
        return False
