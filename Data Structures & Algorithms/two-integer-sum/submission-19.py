class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = defaultdict(list)

        for i, num in enumerate(nums):
            missing = target - num

            if missing in nums_map:
                return [nums_map[missing][0], i]
            else:
                nums_map[num].append(i)