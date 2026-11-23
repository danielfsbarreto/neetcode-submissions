class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count_nums = defaultdict(int)

        for num in nums:
            count_nums[num] += 1

            if count_nums[num] > 1:
                return True
        return False
            