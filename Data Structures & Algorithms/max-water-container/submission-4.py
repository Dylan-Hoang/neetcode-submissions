class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        maxwater = 0
        while left < right:
            currwater = min(heights[left],heights[right]) * (right - left)
            maxwater = max(maxwater,currwater)
            if heights[left] > heights[right]:
                right-=1
            else:
                left+=1
        return maxwater
        