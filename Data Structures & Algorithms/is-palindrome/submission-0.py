class Solution:
    def isPalindrome(self, s: str) -> bool:
        first = 0
        second = len(s) -1
        while first < second:
            while not (s[first].isalnum()) and first <second:
                first+=1
            while not (s[second].isalnum()) and first <second:
                second-=1
            if s[first].lower() != s[second].lower():
                return False
            first+=1
            second-=1
        return True
            
        