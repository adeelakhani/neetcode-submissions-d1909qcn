class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        l, r = 0, len(nums)-1
        numList = []
        nums.sort()
        print(nums)
        for i in range(0, len(nums)):
            if i == 0 or (nums[i-1] != nums[i]):
                l = i + 1
                r = len(nums)-1
                while l < r:
                    if (nums[i] + nums[l] + nums[r]) == 0:
                        numList.append([nums[i], nums[l], nums[r]])
                        l+=1
                        r-=1
                    elif (nums[i] + nums[l] + nums[r] < 0):
                        l+=1
                        while nums[l] == nums[l-1]:
                            l+=1
                            if l>r:
                                break
                    else:
                        r-=1
                        while nums[r] == nums[r+1]:
                            print(i)
                            print(l)
                            print(r)
                            r-=1
                            if l>r:
                                break
        return numList
