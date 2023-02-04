class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        word_len = len(words[0])
        all_word_len  = word_len * len(words)
        target = Counter(words)  
        res = []
        
        for i in range(word_len):
            word_dict = defaultdict(int)    
            l = r = i

            while r < len(s):
                word = s[r:r + word_len]
                word_dict[word] += 1
                
                if r - l + word_len == all_word_len :
                    if word_dict == target:
                        res.append(l)
                    
                    word = s[l:l + word_len]
                    word_dict[word] -= 1
                    if word_dict[word] == 0:
                        word_dict.pop(word)
                    
                    l += word_len
                r += word_len
        return res
1
