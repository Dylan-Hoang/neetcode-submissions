class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        currmax = 0
        for i in range(len(nums)):
            currnum = nums[i]
      
            if currnum-1 not in numset:
                curramount =0
                while currnum in numset:
                    curramount+=1
                    currnum+=1
                currmax = max(currmax,curramount)
        return currmax
        