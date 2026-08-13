class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        total = []
        subset = []
        contained = set()
        def add(i):
            print(i)
            if i == len(nums) and tuple(subset) not in contained:
                total.append(subset.copy())
                contained.add(tuple(subset))
                return
            if i == len(nums):
                return
            subset.append(nums[i])
            add(i+1)
            subset.pop()
            add(i+1)
        add(0)
        return total
        