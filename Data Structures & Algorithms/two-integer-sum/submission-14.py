class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # map indexes and values into a hash
        hashmap = defaultdict(list)

        for i, num in enumerate(nums):
            missing = target - num
            if missing in hashmap:
                return [hashmap[missing][0], i]
            else:
                hashmap[num].append(i)
        