class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        current_sum = numbers[l] + numbers[r]
        
        while current_sum != target:
            if current_sum < target:
                l += 1
                if l == r:
                    r = len(numbers) - 1
            else:
                r -= 1
                if l == r:
                    l = 0
            current_sum = numbers[l] + numbers[r]

        return [l+1, r+1]