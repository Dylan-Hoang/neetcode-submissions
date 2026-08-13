class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        total = []
        sub = []
        def add(i):
            if sum(sub)==target:
                total.append(sub.copy())
                return
            if sum(sub) > target:
                return
            if i == len(nums):
                return
            sub.append(nums[i])
            add(i)
            sub.pop()
            add(i+1)
           
        add(0)
        return total


        