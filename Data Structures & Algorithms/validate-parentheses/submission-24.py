class Solution:
    def isValid(self, s: str) -> bool:
        close_to_open = {
            ")": "(",
            "}": "{",
            "]": "[",
        }
        stack = []

        for bracket in s:
            if bracket in close_to_open:
                if not stack or stack.pop() != close_to_open[bracket]:
                    return False
            else:
                stack.append(bracket)


            # if bracket not in close_to_open:
            #     stack.append(bracket)
            # else:
            #     if stack and stack.pop() != close_to_open[bracket]:
            #         return False

        return not stack