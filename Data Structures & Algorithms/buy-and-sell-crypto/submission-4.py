class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        maxprofit = 0
        currlowest = prices[0]
        while right < len(prices):
            currprofit = prices[right] - currlowest
            maxprofit = max(maxprofit,currprofit)
            
            right+=1
            left+=1
            if prices[left] < currlowest:
                currlowest = prices[left]
        return maxprofit

        