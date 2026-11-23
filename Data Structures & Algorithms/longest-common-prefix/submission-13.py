class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        preffix = ""
        base_word = strs[0]
        
        for i in range(len(base_word)):
            char = base_word[i]
            for string in strs[1:]:
                if i == len(string) or string[i] != char:
                    return preffix
            preffix += char
        return preffix

