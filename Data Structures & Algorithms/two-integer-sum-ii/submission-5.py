class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1

        while (numbers[left] + numbers[right]) != target:
            if (numbers[left] + numbers[right]) > target:
                right -= 1
                if right == left: right = len(numbers) - 1  
            else:
                left += 1
                if left == right: left = 0

        return [left+1, right+1]