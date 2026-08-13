class Solution:
    def climbStairs(self, n: int) -> int:
        climbcost = {}
        climbcost[1] = 1
        climbcost[2] = 2
        if n ==1:
            return 1
        if n == 2:
            return 2
        for i in range(3,n+1):
            climbcost[i] = climbcost[i-2] + climbcost[i-1]
        return climbcost[n]
        