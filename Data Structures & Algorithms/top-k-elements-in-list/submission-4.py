class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = defaultdict(int)
        for num in nums:
            frequency[num] += 1

        items = sorted(frequency.items(), key=lambda x: x[1], reverse=True)[:k] 
        return [item[0] for item in items]
        # return sorted(frequency.keys(), reverse=True)
        