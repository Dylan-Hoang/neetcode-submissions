class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        totallist = []
        sublist = []
        def add(i):
            if i == len(nums):
                totallist.append(sublist.copy())
                return
            sublist.append(nums[i])
            add(i+1)
            sublist.pop()
            add(i+1)
        add(0)
        return totallist
            
        