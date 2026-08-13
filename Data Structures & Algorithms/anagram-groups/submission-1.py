class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        totalcollection = defaultdict(list)
        for word in strs:
            lettercount = [0] * 26
            for letter in word:
                lettercount[ord(letter) - ord('a')]+=1
            amountofletter = lettercount
            totalcollection[tuple(amountofletter)].append(word)
        return totalcollection.values()
        