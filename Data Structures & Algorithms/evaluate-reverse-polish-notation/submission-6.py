class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            print(stack)
    
            if token in "+-/*":
                num1 = int(stack[-2])
                num2 = int(stack[-1])
                stack.pop()
                stack.pop()
                if token == "+":
                    stack.append(num1+num2)
                elif token == "-":
                    stack.append(num1-num2)
                elif token == "*":
                    stack.append(num1*num2)
                elif token == "/":
                    stack.append(int(num1/num2))
            else:
                stack.append(token)
        return int(stack[0])
        