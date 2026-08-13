class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        currmax = 0
        while left < right:
            area = abs(right-left) * min(heights[right],heights[left])
            currmax = max(area,currmax)
            if heights[left] > heights[right]:
                right-=1
            else:
                left+=1
        return currmax