class Solution:
    def isHappy(self, n: int) -> bool:
        strn = str(n)
        s = set()
        while strn!='1':
            currsum=0
            for digit in strn:
                currsum+= int(digit) ** 2
            if currsum in s:
                return False
            s.add(currsum)

            strn = str(currsum)
        return True

        