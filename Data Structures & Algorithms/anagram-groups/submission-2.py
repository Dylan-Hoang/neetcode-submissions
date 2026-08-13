class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = {}
        for word in strs:
            freq = [0] * 26
            for character in word:
                character_as_a_number = ord(character) - ord('a')
                freq[character_as_a_number] +=1
            if tuple(freq) not in ans:
                ans[tuple(freq)] = []
                ans[tuple(freq)].append(word)
            else:
                ans[tuple(freq)].append(word)
        return list(ans.values())

        