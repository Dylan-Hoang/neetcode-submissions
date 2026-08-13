class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for word in strs:
            wordcount = [0] * 26
            for letter in word:
                count = ord(letter) - ord('a')
                wordcount[count]+=1
            groups[tuple(wordcount)].append(word)
        return groups.values()
        