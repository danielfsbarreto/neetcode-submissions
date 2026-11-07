class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        alphabet = 'abcdefghijklmnopqrstuvwxyz'

        for word in strs:
            key_list = [0] * len(alphabet)
            for i, char in enumerate(word):
                for j, letter in enumerate(alphabet):
                    if letter == char:
                        key_list[j] += 1

            str_key = str(key_list)
            hashmap[str_key].append(word)

        return list(hashmap.values())