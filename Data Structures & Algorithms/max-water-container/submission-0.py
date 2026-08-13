class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) -1
        maxarea = 0
        while left < right:
            horizontal = right - left
            vertical = min(heights[left],heights[right])
            newarea = vertical * horizontal
            maxarea = max(newarea,maxarea)
            if heights[left] > heights[right]:
                right-=1
            else:
                left+=1
        return maxarea

        