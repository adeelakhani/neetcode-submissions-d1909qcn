class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        def backtrack(startIndex, path):
            if sum(path) == target:
                res.append(path.copy())
            elif sum(path) > target:
                return
            # the reason we have startindex is: when we do it for the 2's we find every
            # possible combination regarding 2, so we dont want to include 2 in the every
            # possible combination regarding 3, that is how we avoid duplciates
            for i in range(startIndex, len(nums)):
                path.append(nums[i])
                backtrack(i, path)
                path.pop()

        backtrack(0, path)
        return res