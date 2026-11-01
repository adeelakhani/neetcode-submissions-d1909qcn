class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        total = 0
        l,r = 0, 0
        res = 0
        while r < len(arr):
            if r-l+1 > k:
                total-=arr[l]
                l+=1
            total+=arr[r]
            if total/k >= threshold and r-l+1 == k:
                res +=1
            r+=1
        return res