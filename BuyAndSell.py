# Best time to buy and sell stock

class Solution:
    def bruteForce(self, prices):
        res = 0
        for i in range(len(prices)):
            buy = prices[i]
            for j in range(i+1, len(prices)):
                sell = prices[j]
                res = max(res, sell - buy)
        return res

    def twoPointer(self, prices):
        l, r = 0, 1
        res = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                res = max(res, prices[r] - prices[l])
            else:
                l = r
            r += 1
        return res
            
s = Solution()
prices = [10,1,5,6,7,1]
print(f"Input : prices = {prices}")
print(f"Output using bruteforce: {s.bruteForce(prices)}")
print(f"Output using two pointer: {s.twoPointer(prices)}")