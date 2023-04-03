class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low , high = 0 , len(matrix) -1
        while low <= high:
            mid = (low+high)//2
            if matrix[mid][-1] >=target:high = mid -1
            else:low = mid+1
        idx = low
        if idx == len(matrix):
            return False
        jdx = bisect_left(matrix[idx],target)
        return target == matrix[idx][jdx]
