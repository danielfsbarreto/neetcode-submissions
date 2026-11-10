class Solution:

    word_separator = '#'

    def encode(self, strs: List[str]) -> str:
        encoded_str = ''
        for word in strs:
            encoded_str += str(len(word)) + self.word_separator + word
        
        return encoded_str


    def decode(self, s: str) -> List[str]:
        decoded_list, i = [], 0

        while i < len(s):
            j = i
            while s[j] != self.word_separator:
                j += 1
            
            word_length = int(s[i:j])
            decoded_list.append(s[j + 1 : j + 1 + word_length])
            i = j + 1 + word_length
            
        return decoded_list
