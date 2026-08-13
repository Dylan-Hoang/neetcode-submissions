class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        frequency = {}
        for letter in s:
            frequency[letter] = frequency.get(letter,0) + 1
        for letter in t:
            frequency[letter] = frequency.get(letter,0) - 1
        for amount in frequency.values():
            if amount!=0:
                return False
        return True
