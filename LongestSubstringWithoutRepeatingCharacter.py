class Solution:
    def bruteForce(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            charSet = set()
            for j in range(i, len(s)):
                if s[j] in charSet:
                    break
                charSet.add(s[j])
            res = max(res, len(charSet))
        return res

    def slidingWindowSet(self, s: str)-> int:
        result = 0
        left = 0
        setCount = set()
        
        for right in range(len(s)):
            while s[right] in setCount:
                setCount.remove(s[left])
                left += 1
            setCount.add(s[right])
            
            result = max(result, right - left + 1)
        
        return result
    
    def slidingWindowMap(self, s: str)-> int:
        mp = {}
        result = 0
        left = 0
        
        for right in range(len(s)):
            if s[right] in mp:
                left = max(mp[s[right]] + 1, left)
            mp[s[right]] = right
            result = max(result, right - left + 1)
        return result

sol = Solution()

s = "racingcards"
print(f"Input: s = {s}")
print(f"Output in bruteForce: {sol.bruteForce(s)}")
print(f"Output in Sliding window (set): {sol.slidingWindowSet(s)}")
print(f"Output in Sliding window (map): {sol.slidingWindowSet(s)}")