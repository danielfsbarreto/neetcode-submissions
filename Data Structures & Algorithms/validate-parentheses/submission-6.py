class Solution:
    def isValid(self, s: str) -> bool:
        matches = {')': '(', ']': '[', '}': '{'}
        stack = []

        for bracket in s:
            if bracket in matches:
                if not stack or matches[bracket] != stack.pop():
                    return False
            else:
                stack.append(bracket)

        return stack == []
                