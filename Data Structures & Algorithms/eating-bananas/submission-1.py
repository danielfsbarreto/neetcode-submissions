class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        result = max(piles)

        l, r = 1, max(piles)

        while l <= r:
            k = (l + r) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(p / k)
            
            if hours <= h:
                result = min(result, k)
                r = k - 1
            else:
                l = k + 1
        return result
