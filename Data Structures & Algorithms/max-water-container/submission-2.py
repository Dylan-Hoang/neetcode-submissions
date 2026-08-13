class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) -1
        currmax = 0
        while left < right:
            height = min(heights[left],heights[right])
            width = right - left
            curr = height * width
            currmax = max(curr,currmax)
            if heights[left] < heights[right]:
                left +=1
            else:
                right-=1
        return currmax

        