class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def checksame(dict1,dict2):
            for i in range(26):
                if dict1[chr(ord("a")+i)] != dict2[chr(ord("a")+i)]:
                    return False
            return True
        freqorig = {}
        freqcopy = {}
        if len(s2) < len(s1):
                    return False
                
        for i in range(26):
            freqorig[chr(ord("a")+i)] = 0
            freqcopy[chr(ord("a")+i)] = 0
        for character in s1:
            freqorig[character] +=1 
        for i in range(len(s1)):
            freqcopy[s2[i]] +=1 
        if checksame(freqcopy,freqorig):
  

            return True
        left = 0
        right = len(s1)
      
        while right < len(s2):
            freqcopy[s2[left]]-=1
            freqcopy[s2[right]]+=1
            if checksame(freqorig,freqcopy):
                return True
            left+=1
            right+=1
        return False    
        