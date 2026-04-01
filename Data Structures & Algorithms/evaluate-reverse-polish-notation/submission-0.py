class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        total = 0
        for i in tokens:
            if i == '+':
                stack[0] += stack[1]
                stack.pop()

            elif i == '*':
                stack[0] *= stack[1]
                stack.pop()
            elif i == '/':
                stack[0] /= stack[1]
                stack.pop()
            elif i == '-':
                stack[0] -= stack[1]
                stack.pop()
            else:
                stack.append(int(i))
        return stack[0]