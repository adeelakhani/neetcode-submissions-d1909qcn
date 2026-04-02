class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i == '+':
                x = stack.pop()
                y = stack.pop()
                stack.append(y + x)
            elif i == '*':
                x = stack.pop()
                y = stack.pop()
                stack.append(y * x)
            elif i == '/':
                x = stack.pop()
                y = stack.pop()
                if (stack[-1] != 0):
                    stack.append(y / x)
            elif i == '-':
                x = stack.pop()
                y = stack.pop()
                stack.append(y - x)
            else:
                stack.append(int(i))
        return int(stack[0])