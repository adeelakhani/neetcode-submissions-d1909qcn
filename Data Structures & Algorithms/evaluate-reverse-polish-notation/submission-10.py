
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        import operator
        stack = []

        ops = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': lambda a,b: int(a/b)}

        for i in tokens:
            if i in ops:
                x, y = stack.pop(), stack.pop()
                stack.append(ops[i](y, x))
            else:
                stack.append(int(i))
#         stack = []
#         for i in tokens:
#             if i == '+':
#                 x = stack.pop()
#                 y = stack.pop()
#                 stack.append(y + x)
#             elif i == '*':
#                 x = stack.pop()
#                 y = stack.pop()
#                 stack.append(y * x)
#             elif i == '/':
#                 x = stack.pop()
#                 y = stack.pop()
#                 stack.append(int(y / x))
#             elif i == '-':
#                 x = stack.pop()
#                 y = stack.pop()
#                 stack.append(y - x)
#             else:
#                 stack.append(int(i))
#         return int(stack[0])