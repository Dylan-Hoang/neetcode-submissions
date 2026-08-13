class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        contained = set(nums)
        maxcurr = 0
        count = 0
        for num in nums:
            
            if num-1 not in contained:
                curr = num
                count =1
                while curr+1  in contained:
                    curr+=1
                    count+=1
            maxcurr = max(count,maxcurr)
        return maxcurr