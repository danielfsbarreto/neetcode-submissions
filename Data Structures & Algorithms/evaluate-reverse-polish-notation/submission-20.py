class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            match token:
                case '+':
                    t1, t2 = stack.pop(), stack.pop()
                    stack.append(t2 + t1)
                case '-':
                    t1, t2 = stack.pop(), stack.pop()
                    stack.append(t2 - t1)
                case '*':
                    t1, t2 = stack.pop(), stack.pop()
                    stack.append(t2 * t1)
                case '/':
                    t1, t2 = stack.pop(), stack.pop()
                    stack.append(int(t2 / t1))
                case _:
                    stack.append(int(token))

        return stack[-1]