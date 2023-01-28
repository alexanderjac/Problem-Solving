class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        wordList.append(beginWord)
        wordList = set(wordList)
        queue = collections.deque([[beginWord,1]])
        while queue:
            word, length = queue.popleft()
            if word == endWord:
                return length
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    nextWord = word[:i] +c + word[i+1:]
                    if nextWord in wordList:
                        queue.append([nextWord,length+1])
                        wordList.remove(nextWord)
        return 0
"""
hit -> hot -> dot -> dog -> cog


"""