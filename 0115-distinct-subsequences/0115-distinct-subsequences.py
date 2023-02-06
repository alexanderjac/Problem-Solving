class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        cache = {}
        def dfs(i, j):
            if j == len(t):
                return 1
            if i== len(s):
                return 0
            if (i,j) in cache:
                return cache[(i,j)]
            if s[i] == t[j]:
                cache[(i,j)] = dfs(i+1,j+1) + dfs(i+1,j)
            else:
                cache[(i,j)] = dfs(i+1,j)
            return cache[(i,j)]
        return dfs(0,0)
        # dp = [[0 for i in range(len(t))] for j in range(len(s))]
        # for i in range(1,len(s)):
        #     for j in range(len(t)):
        #         if s[i]==t[j]:
        #             if s[:i+1] == t[:j+1]:
        #                 dp[i][j] = 0
        #             else:
        #                 if s[i-1] == t[j]:
        #                     dp[i][j] = 1+ dp[i][j-1]
        #         else:
        #             if s[i-1] == t[j]:
        #                 dp[i][j] =  1+ dp[i-1][j]
        # # print(dp)
        # return dp[-1][-1]
                     
        """
        Input: s = "rabbbit", t = "rabbit"
        lenT = 6
        "rabbbit" 
         rabb_it
         rab_bit
         ra_bbit
         count = 3
            
        rabbxit
        raxbbit
        rabxbit
        
        _ r   a     b    b   i    t
        
      r   0   0     0    0   0    0
      
      a   1   0     0    0   0.   0
      
      b   1   1     0.   0.  0.   0
      
      b   1   1     2    0.  0.   0
      
      b   1        3    3
      
      i
      
      t
       
       if s[i]==t[j]:
            if s[:i] == t[:j]:
                dp[i][j]  =0
            else:
                if s[i-1] == t[j]
                    dp[i][j] = 1+ dp[i][j-1]
        else:
            dp[i][j] = dp[i-1][j]
       
       
       return dp[-1][-1]
   
        """
        
        