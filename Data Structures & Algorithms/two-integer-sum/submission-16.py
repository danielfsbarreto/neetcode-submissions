class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_nums = defaultdict(list)

        for i, num in enumerate(nums):
            missing = target - num
            if missing in hash_nums:
                return [hash_nums[missing][0], i]
            else:
                hash_nums[num].append(i)