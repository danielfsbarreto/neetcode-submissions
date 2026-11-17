class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        stack = [0]

        while l < r:
            volume = min(heights[l], heights[r]) * (r - l)
            if volume > stack[-1]:
                stack.append(volume)
            
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return stack[-1]