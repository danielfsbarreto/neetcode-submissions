class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numshash = defaultdict(int)

        for num in nums:
            if num in numshash:
                return True
            numshash[num] += 1
        
        return False