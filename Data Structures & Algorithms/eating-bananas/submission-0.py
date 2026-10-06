class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        minamount = 1
        maxamount = max(piles)
        currbest = 1
        while minamount <= maxamount:
            curramount = (minamount + maxamount) // 2
            hours = 0
            for pile in piles:
                hours += math.ceil(pile/curramount)
                print(math.ceil(pile//curramount))

            if hours > h:
                minamount = curramount + 1
            else:
                currbest = curramount
                maxamount = curramount -1
        return currbest