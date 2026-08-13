class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        currmul = 0
        for num in nums:
            currmul^=num
        return currmul
        