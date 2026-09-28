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
                while s[right] in freq:
                    freq.remove(s[left])
                    left+=1
                freq.add(s[right])
            right+=1
        return largest_substr

            


