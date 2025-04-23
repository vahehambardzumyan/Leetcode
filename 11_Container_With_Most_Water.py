class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea = 0
        left = 0
        right = len(height) - 1 
        while left < right:
            temp = (right - left) * min(height[right], height[left])
            maxArea = max( maxArea, temp)
            if height[right] > height[left]:
                left+=1
            else: # height[r] < height[l]
                right-=1

        return maxArea