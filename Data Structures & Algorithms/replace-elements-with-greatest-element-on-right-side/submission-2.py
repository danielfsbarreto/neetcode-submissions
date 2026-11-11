class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr) - 1):
            max_of_right = sorted(arr[i+1:])[-1]
            arr[i] = max_of_right
        arr[-1] = -1
        return arr

