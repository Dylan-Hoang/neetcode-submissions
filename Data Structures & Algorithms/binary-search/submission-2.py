class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left+right) // 2
            midnum = nums[mid]
            print(mid,midnum)
            if midnum < target:
                left = mid + 1
            elif midnum > target:
                right = mid - 1
            elif target == midnum:
                return mid
        return -1
            