class Solution:
    def isValid(self, s: str) -> bool:
        matching = {"]":"[","}":"{",")":"("}
        start = "({["
        stack = []
        for p in s:
            if p in start:
                stack.append(p)
            else:
                if len(stack)==0:
                    return False
                if stack[-1]==matching[p]:
                    stack.pop()
                else:
                    return False
        return stack==[]
        