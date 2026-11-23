class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = defaultdict(int)

        for num in nums:
            counter[num] += 1
        
        heap = []
        heapq.heapify_max(heap)

        for count in counter:
            heapq.heappush_max(heap, (counter[count], count))

        result = []
        for i in range(k):
            result.append(heapq.heappop_max(heap)[1])

        return result