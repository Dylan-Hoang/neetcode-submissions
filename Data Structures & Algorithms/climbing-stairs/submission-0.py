class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}
        def count(n):
            if n==1:
                cache[1] = 1
                return 1
            elif n==2:
                cache[2] = 2
                return 2
            elif n-1 in cache and n-2 in cache:
                return cache[n-1] + cache[n-2]
            else:
                return count(n-1) + count(n-2)
        return count(n)


        