class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num,0) +1
        table = []
        for i in range(len(nums)+1):
            table.append([])
        for key,value in freq.items():
            table[value].append(key)
        ans = []
        print(table)
        for i in range(len(nums),-1,-1):
            for origvalue in table[i]:
                ans.append(origvalue)
                if len(ans)== k:
                    return ans
