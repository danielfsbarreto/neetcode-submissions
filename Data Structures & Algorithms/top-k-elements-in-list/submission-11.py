class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_map = defaultdict(int)
        for num in nums:
            count_map[num] += 1

        heap = []
        for count in count_map:
            heapq.heappush_max(heap, (count_map[count], count))

        most_frequent = []
        while len(most_frequent) < k:
            most_frequent.append(heapq.heappop_max(heap)[1])
            
        return most_frequent