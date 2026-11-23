class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        preffix = ""
        base_word = strs[0]
        
        for i in range(len(base_word)):
            for s in strs:
                if i == len(s) or s[i] != base_word[i]:
                    return preffix
            preffix += base_word[i]
        return preffix

