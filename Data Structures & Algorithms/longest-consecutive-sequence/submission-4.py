class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers_set = set(nums)
        longest = 0        

        for number in numbers_set:
            # if no left neighbor, then it's the start of a sequence
            if (number - 1) not in numbers_set:
                length = 1
                while (number + length) in numbers_set:
                    length += 1
                longest = max(longest, length)
        
        return longest