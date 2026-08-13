class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        sumcost = [-1] * len(cost)
        sumcost[-1] = cost[-1]
        sumcost[-2] = cost[-2]
        def calcsum(n):
            if n==-1:
                return min(sumcost[0],sumcost[1])
            else:
                sumcost[n] = min(sumcost[n+1],sumcost[n+2]) + cost[n]
                return calcsum(n-1)
        return calcsum(len(cost)-3)