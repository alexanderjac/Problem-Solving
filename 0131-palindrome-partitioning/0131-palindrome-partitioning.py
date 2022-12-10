class Solution:
    def ispalindrome(self, s):
        left = 0
        right = len(s)-1
        while left <=right  :
            if s[left]!= s[right]:
                return False
            left +=1
            right -=1
        return True
    
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def dp(s, temp, res):
            if not s:
                res.append(temp[::])
                return
            for i in range(1, len(s)+1):
                # if s[:i] == s[i-1::-1]:
                #     # print()
                #     temp.append(s[:i])
                #     dp(s[i:], temp, res)
                #     temp.pop()
                if self.ispalindrome(s[:i]):
                    # print()
                    temp.append(s[:i])
                    dp(s[i:], temp, res)
                    temp.pop()
        
        
        dp(s,[],res)
        return res