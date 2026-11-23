class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter_s = defaultdict(int)
        counter_t = defaultdict(int)

        for c in s:
            counter_s[c] += 1
        
        for c in t:
            counter_t[c] += 1

        return counter_s == counter_t