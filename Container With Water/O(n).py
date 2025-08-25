class Solution:
    def maxArea(self, height: List[int]) -> int:
        # we want to maximize the area of the water held (height * width)
        largestArea = 0
        left = 0
        right = len(height) - 1
        while left < right:
            if height[left] < height[right]:
                area = height[left] * (right - left)
                if area > largestArea:
                    largestArea = area
                left+=1
            elif height[right] < height[left]:
                area = height[right] * (right - left)
                if area > largestArea:
                    largestArea = area
                right -= 1
            else:
                area = height[right] * (right - left)
                if area > largestArea:
                    largestArea = area
                right -= 1
                left += 1
        return largestArea