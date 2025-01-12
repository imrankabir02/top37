from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        maxArea = 0
        width, maxHeight = 0, 0
        while left < right:
            width = right - left
            if height[left] < height[right]:
                maxHeight = height[left]
                left += 1
            else :
                maxHeight = height[right]
                right -= 1

            maxArea = max(maxArea, maxHeight*width)
        return maxArea
    
solution = Solution()

# Test Cast 1
nums = [1,2,3,4,5,6,7]

print(f"Input: nums={nums}")
print(f"Output: ", solution.maxArea(nums))
