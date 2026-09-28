class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        def check(arr,k):
            total = sum(arr)
            maxelement = max(arr)
            if total - k > maxelement:
                return False
            return True
        freq = [0 for i in range(26)]
        left = 0
        right = 0
        maxlength = 0
        while right < len(s):
            idx = ord(s[right]) - ord('A')
            freq[idx]+=1
            if check(freq,k):
                maxlength = max(right - left + 1,maxlength)
            else:
                while not check(freq,k):
                    leftinx = idx = ord(s[left]) - ord('A')

                    freq[leftinx] -=1
                    left+=1
            right+=1
        
        return maxlength