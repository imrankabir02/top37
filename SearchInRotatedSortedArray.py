class Solution:
    def bruteForce(self, nums, target):
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        return -1

    def search(self, nums, target):
        if not nums: 
            return -1
        
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
                
        return -1
sol = Solution()

nums = [5,1,3]
target = 5
print(f"Input: nums={nums}, target={target}")
print(f"Output using bruteForce: {sol.bruteForce(nums, target)}")
print(f"Output using binary search: {sol.search(nums, target)}")

# Test cases
# if __name__ == "__main__":
    # print(bruteForce([4,5,6,7,0,1,2], 0))  # Output: 4
    # print(search([4,5,6,7,0,1,2], 3))  # Output: -1
    # print(search([1], 0))  # Output: -1