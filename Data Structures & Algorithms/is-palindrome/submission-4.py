class Solution:
    def isPalindrome(self, s: str) -> bool:
        def _isNotAlphaNum(c: str) -> bool:
            return not (
                ord('0') <= ord(c) <= ord('9') or 
                ord('a') <= ord(c) <= ord('z') or 
                ord('A') <= ord(c) <= ord('Z')
            )

        
        left_pointer, right_pointer = 0, len(s) - 1

        while left_pointer < right_pointer:
            while left_pointer < right_pointer and _isNotAlphaNum(s[left_pointer]):
                left_pointer += 1
            while right_pointer > left_pointer and _isNotAlphaNum(s[right_pointer]):
                right_pointer -= 1

            if s[left_pointer].lower() != s[right_pointer].lower():
                return False
            
            left_pointer += 1
            right_pointer -= 1
        return True
