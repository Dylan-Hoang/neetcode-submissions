class Solution:
    def isValid(self, s: str) -> bool:
        pair = {'}':'{', ")": "(", "]":"["}
        left = "[{("
        stack = []
        for character in s:
            if character in left:
                stack.append(character)
            else:
                if stack==[]:
                    return False
                if pair[character] == stack[-1]:
                    stack.pop()
                else:
                    stack.append(character)
        return stack == []

        