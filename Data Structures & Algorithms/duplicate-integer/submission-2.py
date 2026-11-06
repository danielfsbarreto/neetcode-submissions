from collections import defaultdict

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_dict = defaultdict(int)
        for num in nums:
            num_dict[num] += 1

            if num_dict[num] > 1:
                return True
        return False

        