class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        result = [0] * len(arr)
        max_right = -1
        for i in range(len(arr) -1, -1, -1):
            result[i] = max_right
            max_right = max(arr[i], max_right)
        return result