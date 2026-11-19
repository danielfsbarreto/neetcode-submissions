class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""

        for word in strs:
            encoded_str += str(len(word)) + "#" + word

        return encoded_str

    def decode(self, s: str) -> List[str]:
        decoded_list, i = [], 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            str_length = int(s[i:j])
            decoded_string = s[j+1:j+1+str_length]
            decoded_list.append(decoded_string)
            i = j+1+str_length
        return decoded_list

        