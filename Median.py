from typing import List

class Solution:
    def bruteForce(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        total = len(nums1)
        if total % 2 == 0:
            return (nums1[total//2] + nums1[total//2 - 1]) / 2.0
        else:
            return nums1[total//2]
    
    
        
solution = Solution()

# Test Cast 1
nums1 = [1,3]
nums2 = [2]
print(f"Input: nums1={nums1}, nums2={nums2}")
print(f"Output: ", solution.bruteForce(nums1, nums2))  # Expected Output: 2.0

# Test Case 2
nums3 = [1,2]
nums4 = [3,4]
print(f"Input: nums1={nums3}, nums2={nums4}")
print(f"Output: ", solution.bruteForce(nums3, nums4))  # Expected Output: 2.5

# Test Case 3
nums5 = [0,0]
nums6 = [0,0]
print(f"Input: nums1={nums5}, nums2={nums6}")
print(f"Output: ", solution.bruteForce(nums5, nums6))  # Expected Output: 0.0