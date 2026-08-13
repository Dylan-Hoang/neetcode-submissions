class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = [-1] * len(nums)
        if len(nums)==1:
            return nums[0]
        if len(nums)==2:
            return max(nums)
        cache[-1] = nums[-1]
        cache[-2] = nums[-2]
        for i in range(len(nums)-3,-1,-1):
            maxsteal = max(nums[i]+cache[i+2],cache[i+1])
            cache[i] = maxsteal
        return cache[0]
        