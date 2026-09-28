class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        largest_substr = 0
        freq = set()
        left = 0
        right = 0
        while right < len(s):
            if s[right] not in freq:
                freq.add(s[right])
                largest_substr = max(largest_substr,len(freq))
            
            else:
                while s[left] != s[right]:
                    freq.remove(s[left])
                    left+=1
                left+=1
            right+=1
        return largest_substr

            


