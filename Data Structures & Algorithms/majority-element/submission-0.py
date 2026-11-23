class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums_sorted = sorted(nums)

        return nums_sorted[len(nums) // 2]