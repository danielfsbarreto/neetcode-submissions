class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        results = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][1]:
                ref_index, _ = stack.pop()
                results[ref_index] = i - ref_index
            stack.append((i, t))
        
        return results