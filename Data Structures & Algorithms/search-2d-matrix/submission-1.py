class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix) - 1
        while left <=right:
            middle = (left+right)//2
            print(middle)
            if target > matrix[middle][-1]:
                left = middle + 1
            elif target < matrix[middle][0]:
                right = middle - 1
            else:
                break
        l2 = 0
        r2 = len(matrix[middle]) -1
        while l2 <= r2:
            m2 = (l2+r2) //2
            if target> matrix[middle][m2]:
                l2 = m2+1
            if target < matrix[middle][m2]:
                r2 = m2-1
            if target == matrix[middle][m2]:
                return True
        return False