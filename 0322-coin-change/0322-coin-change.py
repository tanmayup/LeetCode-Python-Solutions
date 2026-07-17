class Solution:
    def ks(self, i, w, values, dp):
        if w == 0:
            return 0

        if i == len(values):
            return float("inf") 

        if dp[i][w] != -1:
            return dp[i][w]

        take = float("inf")
        if w >= values[i]:
            take = 1 + self.ks(i, w-values[i], values, dp)
        not_take = self.ks(i+1, w, values, dp)

        dp[i][w] = min(take, not_take)

        return dp[i][w]

    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [[-1] * (amount + 1) for _ in range(len(coins))]
        
        ans = self.ks(0, amount, coins, dp)
        return ans if ans != float("inf") else -1