class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A = nums1
        B = nums2
        if len(nums1) > len(nums2):
            A = nums2
            B = nums1
        l, r = 0, len(A)-1
        total = (len(A) + len(B))//2
        while l<=r:
            mid = l+(r-l)//2
            left_partition_A = mid
            left_partition_B = total-mid

            l1 = A[left_partition_A] if left_partition_A > 0 else float('-inf')
            l2 = B[left_partition_B] if left_partition_B > 0 else float('-inf')
            r1 = A[left_partition_A+1]   if left_partition_A < len(A) else float('inf')
            r2 = B[left_partition_B+1]   if left_partition_B < len(B) else float('inf')

            if (l1 <= r2) and (l2 <= r1):
                if (len(A) + len(B)) %2 == 0:
                    return (max(l1, l2) + min(r1, r2))/2
                else:
                    return min(r1, r2)
            elif l1 > r2:
                r = mid -1
            else:
                l = mid + 1

        return -1

            # [ len(A) + len(B)] // 2
            # need to take the lower bound since we want to get 
            # A = [1, 12,| 15, 26, 38]
            # B = [2, 13, 17, 30, 45, 60]
