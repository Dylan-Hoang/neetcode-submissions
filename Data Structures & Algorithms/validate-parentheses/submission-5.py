class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {"]":"[","}":"{",")":"("}
        stack = []
        for symbol in s:
            
            if symbol in "[{(":
                stack.append(symbol)
            else:
                if len(stack) == 0:
                    return False
                if stack[-1] == pairs[symbol]:
                    stack.pop()
                else:
                    stack.append(symbol)
        return stack == []
        