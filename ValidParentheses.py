class Solution:
    def bruteForce(self, s):
        while '()' in s or '{}' in s or '[]' in s:
            s = s.replace('()', '')
            s = s.replace('{}', '')
            s = s.replace('[]', '')
        return s == ''
    
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        stack = []
        for i in s:
            if i == '(' or i == '{' or i == '[':
                stack.append(i)
            else:
                if not stack:
                    return False
                else:
                    if i == ')' and stack[-1] == '(':
                        stack.pop()
                    elif i == '}' and stack[-1] == '{':
                        stack.pop()
                    if i == ']' and stack[-1] == '[':
                        stack.pop()
        return len(stack) == 0        
sol = Solution()
s = "([{}])"
# s = "[(])"

print(f"Input: s = {s}")
print(f"Output: {sol.isValid(s)}")