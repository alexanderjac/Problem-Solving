class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        rows = len(word1)
        cols = len(word2)
        dp = [[0 for i in range(cols+1)] for j in range(rows+1)]
        for i in range(rows+1):
            for j in range(cols+1):
                if i == 0 :
                    dp[i][j] = j
                    continue
                elif j == 0:
                    dp[i][j] = i
                    continue
                if word1[i-1] != word2[j-1]:
                    dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1])
                else:
                    dp[i][j] = dp[i-1][j-1]
        return dp[-1][-1]
        