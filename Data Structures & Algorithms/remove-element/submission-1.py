class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        not_matching = []

        for num in nums:
            if num != val:
                not_matching.append(num)

        for i in range(len(not_matching)):
            nums[i] = not_matching[i]

        return len(not_matching)