class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        arr_size = len(arr)
        result = [0] * arr_size
        max_right = -1
        for i in range(arr_size - 1, -1, -1):
            result[i] = max_right
            max_right = max(arr[i], max_right)
            
        return result