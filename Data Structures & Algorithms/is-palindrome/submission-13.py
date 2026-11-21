class Solution:
    def isPalindrome(self, s: str) -> bool:
        alpha_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
        alpha_str = ""

        for c in s:
            if c in alpha_chars:
                alpha_str += c.lower()

        return alpha_str == alpha_str[::-1]