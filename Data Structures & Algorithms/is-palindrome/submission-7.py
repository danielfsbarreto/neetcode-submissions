class Solution:
    def isPalindrome(self, s: str) -> bool:
        def _isAlphaNum(c: str) -> bool:
            return (
                ord('0') <= ord(c) <= ord('9') or 
                ord('a') <= ord(c) <= ord('z') or 
                ord('A') <= ord(c) <= ord('Z')
            )

        alphanum_string = ""

        for c in s:
            if _isAlphaNum(c): alphanum_string += c.lower()

        return alphanum_string == alphanum_string[::-1]