class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        max1 = 0
        for num in nums:
            curr = 0
            incr = 0
            if num-1 not in numset:
                while incr+num in numset:
                    incr+=1
                    curr+=1
                max1 = max(max1,curr)
        return max1
        