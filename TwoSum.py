from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
        return [-1,-1]

solution = Solution()

# Test Cast 1
nums = [1,2,3,4,5,6,7]
target = 9

print(f"Input: nums={nums}, target={target}")
print(f"Output: ", solution.twoSum(nums, target))

# Test Case 2
nums2 = [3, 2, 4]
target2 = 6
print(f"Input: nums={nums2}, target={target2}")
print("Output:", solution.twoSum(nums2, target2))  # Expected Output: [1, 2]

# Test Case 3
nums3 = [3, 3]
target3 = 6
print(f"Input: nums={nums3}, target={target3}")
print("Output:", solution.twoSum(nums3, target3))  # Expected Output: [0, 1]

# Test Case 4 (No solution case)
nums4 = [1, 2, 3]
target4 = 10
print(f"Input: nums={nums4}, target={target4}")
print("Output:", solution.twoSum(nums4, target4))  # Expected Output: [-1, -1]