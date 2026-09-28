class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq = [0 for i in range(26)]
        for character in s1:
            freq[ord(character) -  ord('a')]+=1
        freq2 = [0 for i in range(26)]
        if len(s1) > len(s2):
            return False
        left = 0
        right = 0
        while right < len(s2):
            freq2[ord(s2[right]) - ord('a')]+=1
            print(freq,freq2)
            if sum(freq2) > sum(freq):
                freq2[ord(s2[left]) - ord('a')] -=1
                left+=1
            if freq2 == freq:
                return True
            right+=1
        return False
            
        