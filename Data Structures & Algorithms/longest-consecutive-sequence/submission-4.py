class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxsofar = 0
        setof = set(nums)
        for num in nums:
            if num-1 not in setof:
                currcount = 1
                curr = num
                while curr +1 in setof:
                    currcount+=1
                    curr+=1
                maxsofar = max(maxsofar,currcount)
        return maxsofar
        