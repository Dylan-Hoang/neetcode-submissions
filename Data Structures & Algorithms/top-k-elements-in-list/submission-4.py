class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num,0) + 1
        freqrev = [[] for i in range(len(nums) + 1)]
        for key,value in freq.items():
            freqrev[value].append(key)
        res = []
        for i in range(len(nums),-1,-1):
            for num in freqrev[i]:
                res.append(num)
            if len(res) == k:
                return res
