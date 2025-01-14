from typing import List

class Solution():
    def bruteForce(self, s:str) -> str:
        def checkPalindrome(sub: str) -> bool:
            return sub == sub[::-1]
        
        res, resLen = "", 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                if checkPalindrome(s[i:j+1]) and resLen < (j - i + 1):
                    res = s[i:j+1]
                    resLen = j - i + 1
        
        return res
    
    
    def twoPointer(self, s: str) -> str:
        resIdx, resLen = 0, 0
        
        for i in range(len(s)):
            left, right = i, i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > resLen:
                    resIdx = left
                    resLen = right - left + 1
                left -= 1
                right += 1
            
            left, right = i, i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > resLen:
                    resIdx = left
                    resLen = right - left + 1
                left -= 1
                right += 1
            
        return s[resIdx: resIdx + resLen]
    
solution = Solution()
s = "abbc"
print(f"Input: {s}")
print(f"Output with bruteForce: ", solution.bruteForce(s)) 
print(f"Output with twoPointer: ", solution.twoPointer(s)) 