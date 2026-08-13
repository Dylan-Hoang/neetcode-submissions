class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        product_array = [1] * len(nums)
        leftproduct = 1
        for i in range(len(nums)):
            
            product_array[i]*=leftproduct
            leftproduct*=nums[i]
        rightproduct = 1
        for i in range(len(nums)-1,-1,-1):
            
            product_array[i]*=rightproduct
            rightproduct*=nums[i]
        return product_array
        