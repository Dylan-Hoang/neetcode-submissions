class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) -1
        leftmax, rightmax = height[left],height[right]
        water = 0
        while left < right:
            if leftmax > rightmax:
                water+= max(0,min(leftmax,rightmax)-height[right])
                right-=1
                rightmax = max(rightmax,height[right])
            elif leftmax <= rightmax:
                water+= max(0,min(leftmax,rightmax)-height[left])
                left+=1
                leftmax = max(leftmax,height[left])
        return water


        