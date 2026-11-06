class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numbers_seen = set()

        for num in nums:
            if num not in numbers_seen:
                numbers_seen.add(num)
            else:
                return True
        return False