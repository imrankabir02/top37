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
    
    def twoPointer(self, nums1:List[int], nums2:List[int]) -> float:
        len1, len2 = len(nums1), len(nums2)
        i = j = 0
        median1 = median2 = 0
        
        for count in range((len1 + len2) // 2 + 1):
            median2 = median1
            # print(f"median1={median1}, median2={median2}")
            if i < len1 and j < len2:
                if nums1[i] < nums2[j]:
                    median1 = nums1[i]
                    i += 1
                else:
                    median1 = nums2[j]
                    j += 1
            elif i < len1:
                median1 = nums1[i]
                i += 1
            else:
                median1 = nums2[j]
                j += 1
            print(f"median1={median1}, median2={median2}")
            
        if (len1 + len2) % 2 == 0:
            return (median1 + median2) / 2.0
        else:
            return median1

            
    
    
solution = Solution()

# Test Cast 1
nums1 = [1, 2, 4, 3]
nums2 = [2, 4, 6, 5]
print(f"Input: nums1={nums1}, nums2={nums2}")
print(f"Output: ", solution.twoPointer(nums1, nums2))  # Expected Output: 2.0

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