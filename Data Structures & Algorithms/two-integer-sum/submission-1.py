class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        potentialpair = {}
        for i in range(len(nums)):
            num = nums[i]
            targetnum = target - num
            if targetnum in potentialpair.keys():
                return [potentialpair[targetnum],i]
            potentialpair[num] = i
           


        