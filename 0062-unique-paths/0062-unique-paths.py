class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1 for i in range(n)] for j in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]
#         def dfs(i, j):
#             if i >= m or j >= n:      return 0
#             if i == m-1 and j == n-1: return 1
#             return dfs(i+1, j) + dfs(i, j+1)
#         return dfs(0, 0)
        
        
        
#         count =0
#         def dfs(i, j):
#             nonlocal count
#             if i >= m or j >= n :
#                 return 
#             if i==m-1 and j == n-1:
#                 count +=1
#                 return
#             dfs(i+1,j) 
#             dfs(i, j+1)
        
#         dfs(0,0)
#         return count
        