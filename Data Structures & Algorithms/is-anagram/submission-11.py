class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_s = defaultdict(int)
        hash_t = defaultdict(int)

        for c in s:
            hash_s[c] += 1

        for c in t:
            hash_t[c] += 1

        return hash_s == hash_t