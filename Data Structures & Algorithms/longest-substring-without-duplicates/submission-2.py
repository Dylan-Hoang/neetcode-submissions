class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        charlist = []
        maxamount = 0
        while right < len(s):
            if s[right] in charlist:
                while s[right] in charlist:
              
                
                    charlist.remove(s[left])
                    left+=1
            

            currlength = right - left + 1
            maxamount = max(maxamount,currlength)
            
           
            charlist.append(s[right])
            right+=1
        return maxamount


        