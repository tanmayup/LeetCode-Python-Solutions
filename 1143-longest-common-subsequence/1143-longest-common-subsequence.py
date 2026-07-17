class Solution:
    def rec(self, i, j, t1, t2, dp):
        if i == len(t1) or j == len(t2):
            return 0

        ans = 0
        if dp[i][j] != -1:
            return dp[i][j]

        if t1[i] == t2[j]:
            dp[i][j] = 1 + self.rec(i+1, j+1, t1, t2, dp)
        
        else:
            dp[i][j] = max(self.rec(i, j+1, t1, t2, dp), self.rec(i+1, j, t1, t2, dp))

        return dp[i][j]

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[-1] * len(text2) for _ in range(len(text1))]
        return self.rec(0, 0, text1, text2, dp)