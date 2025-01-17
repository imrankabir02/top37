# Permutations
class Solution:
    def permute(self, nums):
        perms = [[]]
        
        for n in nums:
            new_perms = []
            
            for p in perms:
                for i in range(len(p) + 1):
                    p_copy = p.copy()
                    p_copy.insert(i, n)
                    new_perms.append(p_copy)
            perms = new_perms
        return perms


sol = Solution()
nums = [2,3,6]

print(f"Input: candidates = {nums}")
print(f"Output using backtracking: {sol.permute(nums)}")