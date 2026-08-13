class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            
            middle = (left+right)//2
            result = nums[middle]
            print(left,right,result,middle)
            if result < target:
                left = middle + 1
            elif result > target:
                right = middle -1
            else:
                return middle
        return -1
        