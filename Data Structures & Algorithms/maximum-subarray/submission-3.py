class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currsum = nums[0]
        maxamount = nums[0]
        for i in range(1,len(nums)):
            if currsum < 0:
                currsum=0
            currsum+=nums[i]
            print(currsum)
            maxamount = max(currsum,maxamount)
            
        return maxamount
        