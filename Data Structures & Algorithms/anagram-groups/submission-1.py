class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # letter_map_groups = defaultdict(list)
        
        # for word in strs:
        #     letter_map = defaultdict(int)
        #     for letter in word:
        #         letter_map[letter] += 1
        #     key = frozenset(letter_map.items())
        #     letter_map_groups[key].append(word)
        
        # return list(letter_map_groups.values())

        anagram_maps = defaultdict(list)

        for word in strs:
            sorted_word = ''.join(sorted(word))
            anagram_maps[sorted_word].append(word)

        return list(anagram_maps.values())