class WordDictionary:

    def __init__(self):
        self.trie ={}
        

    def addWord(self, word: str) -> None:
        curr = self.trie
        for c in word:
            if c not in curr:
                curr[c]={}
            curr =curr[c]
        curr["-"] = {}
        
    def search(self, word: str) -> bool:
        def dfs(word, trie, i):
            if i == len(word):
                return "-" in trie
            res = False
            char = word[i]
            if char == ".":
                for c in trie:
                    res = res or dfs(word, trie[c],i+1)
            elif char in trie:
                 res = dfs(word, trie[char] , i+1)        
            return res
        return dfs(word, self.trie, 0)