class Solution:
    def coinChange(self, coins, amount):
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount + 1):
            for c in coins:
                if i - c >= 0:
                    dp[i] = min(dp[i], 1 + dp[i - c])
        return dp[amount] if dp[amount] != amount + 1 else -1
    
s = Solution()
coins = [1,2,5]
amount = 11
print(f"Input: coins = {coins}, amount = {amount}")
print(f"Output using dp: {s.coinChange(coins, amount)}")