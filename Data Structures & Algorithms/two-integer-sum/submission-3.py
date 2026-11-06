class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        first_index = 0 
        second_index = 0 

        for i, first_number in enumerate(nums):
            first_index = i
            for j, second_number in enumerate(nums):
                second_index = j
                if i == j:
                    continue
                if first_number + second_number == target:
                    return [first_index, second_index]