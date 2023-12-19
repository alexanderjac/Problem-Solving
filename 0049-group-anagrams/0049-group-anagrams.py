from collections import defaultdict
class Solution:
    def helper(self, word): 
        if not word:
            return ""
        
        max_size = 26
        string_array = [0 for i in range(max_size)]
        
        for char in word:
            string_array[ord(char) - ord('a')] += 1
        
        string = ""
        for idx, value in enumerate(string_array):
            if value != 0:
                for i in range(value):
                    string += chr(ord('a') + idx)
        
        return string
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash = defaultdict(list)
        for string in strs:
            temp = self.helper(string)
            hash[temp].append(string)
        result = list(hash.values())
        return result
