class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        seen = set()
        result = 0
        start = 0  # Keep track of the starting index of the current substring
        
        for i, char in enumerate(s):
            while char in seen:
                seen.remove(s[start])
                start += 1
            
            seen.add(char)
            result = max(result, i - start + 1)
        
        return result
        
