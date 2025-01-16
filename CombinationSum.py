# Combination Sum

class Solution:
    def combinatioSum(self, candidates, target):
        res = []
        
        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if i >= len(candidates) or total > target:
                return
            
            cur.append(candidates[i])
            dfs(i, cur, total + candidates[i])
            cur.pop()
            dfs(i+1, cur, total)
            
        dfs(0, [], 0)
        return res
    
sol = Solution()
# Input: candidates = [2,3,6,7], target = 7
# Output: [[2,2,3],[7]]
candidates = [2,3,6,7]
target = 7

print(f"Input: candidates = {candidates}, target = {target}")
print(f"Output using backtracking: {sol.combinatioSum(candidates, target)}")