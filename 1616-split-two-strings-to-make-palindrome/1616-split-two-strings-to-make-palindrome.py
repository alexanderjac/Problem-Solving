class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        """
        a = "ulacfd", b = "jizalu"
             
             ""     "ulacfc"        "" "jizalu"     -> ("jizalu") ("ulacfc")
             "u"    "lacfd"         "j" "izalu"      -> ("uizalu") ("jlacfd")
             "ul"   "acfd"          "ji" "zalu"
             "ula"  "cfd"           "jiz" "alu"
             
             "ab"                           "aaabbbaaaddba"
               ^                                        ^
       a=  "ulaaba"  b = "fxtalu"
       "u" "laabu"          "f"  "xtalu"
       "ula" "aba"          "fxt" "alu"
       
       a=  ulaabaxyz     b=  fxtfxtalu
       "u" "laabaxyz"       "f" "xtfxtalu"
       "ula" "abaxyz       "fxt" "fxtalu" 
       "ulaaba" "xyz"     "fxtfxt" "alu"
        
        
        
        """
        return self.checkPalindrome(a, b) or self.checkPalindrome(b,a)
        
    def checkPalindrome(self, a, b):
        length = len(a)
        i = 0
        r = length -1
        while i<=r:
            if a[i] != b[r]:
                break
            i+=1
            r-=1
        # while i<r:
        #     if b[i] != b[r]:
        #         return False
        #     i+=1
        #     r -=1
        if i>r:
            return True
        return a[i:r+1] == a[i:r+1][::-1] or b[i:r+1] == b[i:r+1][::-1]
        return True
        