class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix[0]) * len(matrix)
        l, r = 0, n - 1

        while l <= r:
            mid = l + (r-l) // 2
            arrayNum = mid // len(matrix[0])
            relativeElement = mid - (arrayNum * len(matrix[0]))

            if matrix[arrayNum][relativeElement] == target:
                return True
            elif matrix[arrayNum][relativeElement] < target:
                l = mid + 1
            else:
                r = mid - 1

        return False

