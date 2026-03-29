class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lptr = 0
        rptr = len(numbers)-1
        while lptr < rptr:
            if numbers[rptr] + numbers[lptr] == target:
                return [lptr+1, rptr+1]
            elif numbers[rptr] + numbers[lptr] < target:
                lptr += 1
            elif numbers[rptr] + numbers[lptr] > target:
                rptr -= 1
