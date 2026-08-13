class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        evalstack =[]
        for token in tokens:
            if token in "+-/*":
                num1 = int(evalstack[-2])
                num2 = int(evalstack[-1])
                evalstack.pop()
                evalstack.pop()
                if token == "+":
                    evalstack.append(num1+num2)
                if token == '-':
                    evalstack.append(num1-num2)
                if token == '*':
                    evalstack.append(num1*num2)
                if token == '/':
                    evalstack.append(int(num1/num2))
            else:
                evalstack.append(token)
        return int(evalstack[0])
        