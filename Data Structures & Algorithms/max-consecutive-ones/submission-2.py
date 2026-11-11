class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        current_max = 0
        streak = 0
        

        for num in nums:
            if num == 1:
                streak += 1
            else:
                streak = 0
            current_max = max(current_max, streak)

        return current_max

                
