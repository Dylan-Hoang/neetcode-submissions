class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        currmax = 0
        while right < len(prices):
            if prices[left] < prices[right]:
                currmax = max(currmax,prices[right]-prices[left])
            else:
                left = right
            right+=1
        return currmax
        