class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        seen = set()
        start = 0 # to track the start index of the current substring
        result = 0
        for i, char in enumerate(s):
            if char in seen:
                while char in seen:
                    seen.remove(s[start])
                    start +=1
            seen.add(char)
            result = max(result, i-start+1)
        return result
        
