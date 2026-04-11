class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in matrix:
            l, r = 0, len(matrix[0])-1
            while l <= r:
                mid = l + (r - l) // 2
                if i[mid] == target:
                    return True
                elif i[mid] < target:
                    l = mid+1
                else:
                    r = mid-1
        return False