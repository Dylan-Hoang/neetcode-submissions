class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        potentialpairs = {}
        for i  in range(len(nums)):
            curr = nums[i]
            matchnum = target - nums[i]
            if matchnum in potentialpairs.keys():
                return [potentialpairs[matchnum],i]
            potentialpairs[curr] = i
           


        