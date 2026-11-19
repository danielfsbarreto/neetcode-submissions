class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nums_counter, product = defaultdict(int), 1
        for num in nums:
            nums_counter[num] += 1
            product *= num
        
        if nums_counter[0] > 1:
            return [0] * len(nums)
        elif nums_counter[0] == 1:
            # one zero
            base = [0] * len(nums)
            product, zero_index = 1, 0
            for i, num in enumerate(nums):
                if num == 0: 
                    zero_index = i
                else:
                    product *= num
            base[zero_index] = product
            return base
        else:
            # no zero
            return [int(product/num) for num in nums]
            