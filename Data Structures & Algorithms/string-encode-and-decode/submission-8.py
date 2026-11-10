class Solution:


    def encode(self, strs: List[str]) -> str:
        encoded_characters = []       
        for word in strs:
            encoded_characters.append(f"{len(word)}#{word}")
            
        return ''.join(encoded_characters)


    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        while i < len(s):
            delimiter_idx = s.find('#', i)
            length = int(s[i:delimiter_idx])
            start = delimiter_idx + 1
            decoded.append(s[start:start + length])
            i = start + length
        return decoded