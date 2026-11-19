class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphanumeric = "ABCDEFGHIKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
        clean_string = ""

        for c in s:
            if c in alphanumeric:
                clean_string += c.lower()
        
        return clean_string == clean_string[::-1]