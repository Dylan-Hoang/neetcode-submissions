class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = {}
        for letter in s:
            freq[letter] = 1 + freq.get(letter,0) 
        for letter in t:
            freq[letter] =  freq.get(letter,0) -1
        for freqamount in freq.values():
            if freqamount!=0:
                return False
        return True
        