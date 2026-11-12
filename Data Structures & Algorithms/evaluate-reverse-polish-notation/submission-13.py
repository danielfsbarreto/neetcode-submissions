class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        scores = []

        for token in tokens:
            if token == '+':
                n1, n2 = scores.pop(), scores.pop() 
                scores.append(n2 + n1)
            elif token == '-':
                n1, n2 = scores.pop(), scores.pop() 
                scores.append(n2 - n1)
            elif token == '*':
                n1, n2 = scores.pop(), scores.pop() 
                scores.append(n2 * n1)
            elif token == '/':
                n1, n2 = scores.pop(), scores.pop() 
                scores.append(int(n2 / n1))
            else:
                scores.append(int(token))

        return scores[-1]