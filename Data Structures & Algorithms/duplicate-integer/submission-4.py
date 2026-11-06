class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numbers_seen = set()

        for num in nums:
            if num in numbers_seen:
                return True
            numbers_seen.add(num)
        return False