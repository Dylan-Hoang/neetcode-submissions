class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        kekw = {}
        for i in range(len(nums)):
            targetnum = target - nums[i]
            if targetnum in kekw:
                return [kekw[targetnum], i]
            kekw[nums[i]] = i

        