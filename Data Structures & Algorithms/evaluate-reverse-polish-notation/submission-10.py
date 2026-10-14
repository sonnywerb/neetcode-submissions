class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operands = '+-*/'

        for n in tokens:
            if n in operands:
                a = stack.pop()
                b = stack.pop()
                if n == '+':
                    stack.append(a + b)
                elif n == '-':
                    stack.append(b - a)
                elif n == '*':
                    stack.append(a * b)
                elif n == '/':
                    stack.append(int(b / a))
            else:
                stack.append(int(n))
        return stack[-1]

        