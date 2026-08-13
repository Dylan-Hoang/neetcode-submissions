class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        lettercount_1 = {}
        lettercount_2 = {}
        for character in s:
            if character not in lettercount_1:
                lettercount_1[character] = 1
            else:
                lettercount_1[character]+=1
        for character in t:
            if character not in lettercount_2:
                lettercount_2[character] = 1
            else:
                lettercount_2[character]+=1
        return lettercount_1 == lettercount_2
        