class Solution:
    def isValid(self, s):
        while '()' in s or '{}' in s or '[]' in s:
            s = s.replace('()', '')
            s = s.replace('{}', '')
            s = s.replace('[]', '')
        return s == ''
    
sol = Solution()
# s = "([{}])"
s = "[(])"

print(f"Input: s = {s}")
print(f"Output: {sol.isValid(s)}")