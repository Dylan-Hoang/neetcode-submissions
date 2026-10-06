class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix) - 1
        boxsizes = len(matrix[0]) -1
        while left  <= right:
            middle = (left+right) //2
            print(left,right,middle,boxsizes)
            if target > matrix[middle][boxsizes]:
                left+=1
            elif target < matrix[middle][boxsizes]:
                right-=1
            else:
                break
        left1 = 0
        right1 = boxsizes
        while left1 <= right1:
            middle2 = (left1+right1) // 2
            print(middle,middle2)
            if matrix[middle][middle2] > target:
                right1-=1
            elif matrix[middle][middle2] < target:
                left1+=1
            else:
                return True
        return False

