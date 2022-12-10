class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def dp(s, temp, res):
            if not s:
                res.append(temp[::])
                return
            for i in range(1, len(s)+1):
                if s[:i] == s[i-1::-1]:
                    temp.append(s[:i])
                    dp(s[i:], temp, res)
                    temp.pop()
        
        
        dp(s,[],res)
        return res