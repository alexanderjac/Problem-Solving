class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if len(word1)>len(word2):
            self.minDistance(word2, word1)
        length = len(word2)
        currdp = [0 for i in range(length+1)]
        prevdp = [0 for i in range(length+1)]
        for i in range(len(word1)+1):
            for j in range(length+1):
                if i == 0 :
                    currdp[j]= j
                elif j == 0:
                    currdp[j] = i
                elif word1[i-1] == word2[j-1]:
                    currdp[j] = prevdp[j-1]
                elif word1[i-1] != word2[j-1]:
                    currdp[j] = 1 + min(prevdp[j],currdp[j-1] )
            prevdp = currdp
            currdp = [0 for i in range(length+1)]
        return prevdp[-1]
#         rows = len(word1)
#         cols = len(word2)
#         dp = [[0 for i in range(cols+1)] for j in range(rows+1)]
#         for i in range(rows+1):
#             for j in range(cols+1):
#                 if i == 0 :
#                     dp[i][j] = j
#                     continue
#                 elif j == 0:
#                     dp[i][j] = i
#                     continue
#                 if word1[i-1] != word2[j-1]:
#                     dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1])
#                 else:
#                     dp[i][j] = dp[i-1][j-1]
#         return dp[-1][-1]
        