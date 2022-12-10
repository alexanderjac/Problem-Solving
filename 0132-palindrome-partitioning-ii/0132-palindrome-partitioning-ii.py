class Solution:
    def isPalindrome(self, i,j, s):
        left, right = i,j
        while left<= right:
            if s[left]!= s[right]:
                return False
            left +=1
            right -=1
        return True

    def minCut(self, s: str) -> int:
        if not s : return 0
        
        dp = [[True] * len(s) for i in range(len(s))]        # DP Matrix of booleans -> dp[i][j] - TRUE if 's[i: j + 1]' is palindrome, else FALSE
        cuts = [float("inf")] * len(s)                       # DP cuts array -> indicates min cuts require till ith entry
        
        # We first find all palindromic substrings
        for r in range(1, len(s)):
            for c in range(len(s) - r):
                if not (s[c] == s[c + r] and dp[c + 1][c + r - 1]):
                    dp[c][c + r] = False

        # For ith column, we check every entry till diagonal element
        # If dp[j][i] is true, implies 's[j: i + 1]'' is palindrome and
        # we check if we get minimum cuts considering this substring or not  
        for i in range(len(s)):
            for j in range(i + 1):
                if dp[j][i]:
                    cuts[i] = min(cuts[i], (cuts[j - 1] + 1) if j - 1 >= 0 else 0)
                    
        return cuts[-1]
        dp = [0 for i in range(len(s)+1)]
        for i in range(len(s)-1,-1,-1):
            mincost = float("inf")
            for j in range(i, len(s)):
                # print(s[i:j], s[i:j][::-1])
                if self.isPalindrome(i, j, s):
                # pre = s[i:j]
                # repre = s[i:j][::-1]
                # if pre == repre:
                    cost = 1 + dp[j+1]
                    mincost  = min(mincost,cost)
            dp[i] = mincost
        return dp[0] -1
     
    """
    Another TLE
    def isPalindrome(self, i,j, s):
        left, right = i,j
        while left<= right:
            if s[left]!= s[right]:
                return False
            left +=1
            right -=1
        return True
    def partition(self, s, i, dp):
        if i== len(s):
            return 0
        if dp[i]!= -1:
            return dp[i]
        mincost = float("inf")
        for j in range(i, len(s)):
            if self.isPalindrome(i,j, s):
                cost = 1 + self.partition(s, j+1,dp)
                mincost =  min(mincost,cost )
        dp[i] = mincost
        if mincost == float("inf"):
            return -1 
        return mincost 
    def minCut(self, s: str) -> int:
        dp = [-1 for i in range(len(s))]
        return self.partition(s,0, dp) -1
    
    """

    """
    TLE code  
    def isPalindrome(self, i,j, s):
        left, right = i,j
        while left<= right:
            if s[left]!= s[right]:
                return False
            left +=1
            right -=1
        return True
    def partition(self, s, i):
        if i== len(s):
            return 0
        mincost = float("inf")
        for j in range(i, len(s)):
            if self.isPalindrome(i,j, s):
                cost = 1 + self.partition(s, j+1)
                mincost =  min(mincost,cost )
        if mincost == float("inf"):
            return -1 
        return mincost 
    def minCut(self, s: str) -> int:
        return self.partition(s,0) -1
     """   