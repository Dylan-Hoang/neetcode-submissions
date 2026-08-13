class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        freq = {}
        maxlength = 0
        curr = 0
        while right < len(s):
            freq[s[right]] = freq.get(s[right],0) + 1
            while freq[s[right]] !=1:
                freq[s[left]] -=1
                left+=1
                curr-=1
            if freq[s[right]] == 1:

                curr+=1
                maxlength = max(maxlength,curr)
            

            right+=1
        return maxlength
        