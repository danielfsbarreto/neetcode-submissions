class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for word in strs:
            result[str(sorted(word))].append(word)

        return list(result.values())