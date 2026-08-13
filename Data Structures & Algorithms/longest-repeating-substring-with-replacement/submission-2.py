class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        right = 0
        freq = {}
        maxwindow = 0
        while right < len(s):
            currwindowlenght = right - left + 1
            freq[s[right]] = freq.get(s[right],0) + 1
            freqmax = 0
            freqtotal = sum(freq.values())
            for num in freq.values():
                freqmax = max(freqmax,num)
            if freqtotal - freqmax <= k:
                maxwindow = max(maxwindow,freqtotal)
           
                
            else:
                freq[s[left]]-=1
                left+=1
            right+=1
        return maxwindow
