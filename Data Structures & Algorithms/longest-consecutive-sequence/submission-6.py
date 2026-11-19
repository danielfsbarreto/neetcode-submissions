class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsset = set(nums)
        max_sequence = 0

        for num in numsset:
            sequence_counter = 0
            if (num - 1) not in numsset:
                sequence_counter += 1
                while (num + 1) in numsset:
                    sequence_counter += 1
                    num += 1

            max_sequence = max(max_sequence, sequence_counter)
        return max_sequence