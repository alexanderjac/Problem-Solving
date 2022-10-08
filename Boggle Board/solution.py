# TC: (nm*8^s + ws)
# OC: (nm + ws)

class Trie:
    def __init__(self):
        self.root ={}
        self.endSymbol = "*" 
    def insert(self,word):
        curr = self.root
        for c in word:
            if c not in curr:
                curr[c] = {}
            curr = curr[c]
        curr[self.endSymbol] = word

            
def boggleBoard(board, words):
    # Write your code here.
    finalwords = {}
    trie = Trie()
    for word in words:
        trie.insert(word)
    visited = [[False for letter in row ] for row in board]
    for i in range(len(board)):
        for j in range(len(board[i])):
            explore(i, j, board, trie.root,visited, finalwords )
    return list(finalwords.keys())
def explore(i, j, board, trieNode,visited, finalwords ):
    if visited[i][j]:
        return
    letter = board[i][j]
    if letter not in trieNode :
        return
    visited[i][j] = True
    trieNode = trieNode[letter]
    if "*" in trieNode:
        finalwords[trieNode["*"]] = True
    directions = ((1,0),(-1,0),(0,1),(0,-1), (1,1),(-1,-1),(1,-1),(-1,1))
    neighbors =[]
    for dr, dc in directions:
        row ,col = dr+i, dc+j
        if row>=0 and row<len(board) and col>=0 and col<len(board[0]) :
            neighbors.append([row, col])
    for neighbor in neighbors:
        explore(neighbor[0],neighbor[1],board, trieNode,visited, finalwords )
    visited[i][j] = False
