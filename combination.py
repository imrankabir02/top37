from itertools import combinations
class Solution:
    def combine(self, n, k):
        res = []
        
        def dfs(start, t):
            if len(t) == k:
                res.append(t.copy())
                return
            for i in range(start, n+1):
                t.append(i)
                dfs(i+1, t)
                t.pop()
        dfs(1, [])
        return res
    
    def oneLine(self, n, k):
        return list(combinations([i for i in range(1, n+1)], k))  
sol = Solution()

n = 5
k = 3

print(f"Input: n = {n}, k = {k}")
print(f"Output using backtracking: {sol.combine(n, k)}")
print(f"Output using backtracking in one line: {sol.oneLine(n, k)}")