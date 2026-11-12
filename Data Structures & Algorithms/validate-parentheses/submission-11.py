class Solution:
    def isValid(self, s: str) -> bool:
        closing_matches = {')': '(', ']': '[', '}': '{'}
        stack = []

        for bracket in s:
            if bracket in closing_matches:
                if not stack or closing_matches[bracket] != stack.pop():
                    return False
            else:
                stack.append(bracket)

        return not stack
                