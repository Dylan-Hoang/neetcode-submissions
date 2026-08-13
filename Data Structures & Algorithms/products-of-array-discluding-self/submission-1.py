class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        preamount = 1
        prearray = []
        for i  in range(len(nums)):
            res[i]*=preamount
            preamount*=nums[i]
        postamount = 1

        for i in range(len(nums)-1,-1,-1):
            currnum = nums[i]
            res[i]*=postamount
            postamount*=currnum
        return res



        
        