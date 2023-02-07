class Solution:
    
#     def palindromeCheck( self, word,left,right):
#         # left = 0
#         # right = len(word)-1 #2
#         while left<=right : #abc
#             if word[left] != word[right]:
#                 return False
#             left +=1 #1
#             right -=1 #1
            
#         return True
    def checkPartitioning(self, s: str) -> bool:
        dp = [[False if i!= j else True for i in range(len(s))] for j in range(len(s))]
        for i in range(len(s)-1,-1,-1):
            for j in range(i+1,len(s)):
                if s[i] == s[j]:
                    if (j-i != 1 and dp[i+1][j-1]) or j-i ==1 :
                        dp[i][j] = True
        # print(dp)          
        for i in range(2,len(s)):  #bcbddxy
            # first_word = s[i:] #b
            if not dp[i][len(s)-1]:
                continue
            for j in range(1, i):
                # second_word = s[j:i] #bcb
                if not dp[j][i-1]:
                    continue
                # third_word = s[:j] #dd
                if dp[0][j-1]:
                    return True
        return False
            
        
        """
        dp[i][j] = F, if i!=j
        if s[i]==s[j] :
            if j-i!=1 and dp[i+1][j-1] or  == 'T':
                dp[i][j] = 'T'
            elif j-i == 1 :
                dp[i][j] = 'T'
        
            
        
            a b c b d d
        a   T F F F F F
        b   F T F F F F
        c       T
        b         T
        d           T
        d             T
        
        
        """