class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        total = []
        subset = []
        def add(i):
            if i == len(nums):
                total.append(subset.copy())
                return
            subset.append(nums[i])
            add(i+1)
            subset.pop()
            while i < len(nums)-1 and nums[i] == nums[i+1]:
                i+=1
            add(i+1)
        add(0)
        return total
        