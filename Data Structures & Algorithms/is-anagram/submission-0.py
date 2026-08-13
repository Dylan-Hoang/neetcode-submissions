class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = {}
        for l in s:
            freq[l] = freq.get(l,0) +1
        for l in t:
            freq[l] = freq.get(l,0) -1
        for value in freq.values():
            if value != 0:
                return False
        return True
        