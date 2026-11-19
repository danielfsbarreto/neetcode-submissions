class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numshash = defaultdict(int)

        for num in nums:
            numshash[num] += 1

        items = sorted(numshash.items(), key=lambda x: x[1])[-k:]

        return [item[0] for item in items]