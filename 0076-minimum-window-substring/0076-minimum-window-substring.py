class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t =="":
            return ""
        stringWindow = {}
        tCount = {}
        for char in t:
            tCount[char] = 1 + tCount.get( char,0)
        have = 0
        need = len(tCount)
        res, resL = [-1,-1] ,  float("infinity")
        l =0 
        for r in range(len(s)):
            char = s[r]
            stringWindow[char] = 1 + stringWindow.get(char,0)
            if char in tCount and tCount[char] == stringWindow[char]:
                have +=1
            
            while have == need:
                if (r-l+1) < resL:
                    resL = r-l+1
                    res = [l,r]
                stringWindow[s[l]] -=1
                if s[l] in tCount and stringWindow[s[l]] <tCount[s[l]]:
                    have -=1
                l+=1
        l, r = res
        return s[l:r+1] if resL != float("infinity") else  ""
                
            
            
            