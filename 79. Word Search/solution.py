class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        path = set()
        def backtrack(row_idx, col_idx,word_idx):
            if word_idx == len(word):
                return True
            if (row_idx<0 or row_idx>=rows or col_idx<0 or col_idx>=cols or ((row_idx, col_idx) in path) or word[word_idx]!= board[row_idx][col_idx]):
                return False
            path.add((row_idx, col_idx))
            res = (backtrack(row_idx+1, col_idx, word_idx+1) or
                  backtrack(row_idx-1, col_idx, word_idx+1) or
                  backtrack(row_idx, col_idx+1, word_idx+1) or 
                  backtrack(row_idx, col_idx -1, word_idx+1))
            path.remove((row_idx, col_idx))
            return res
        for row_idx in range(rows):
            for col_idx in range(cols):
                if backtrack(row_idx, col_idx, 0): return True
        return False
TC: O(n*m*4^n)
SC: O(N) Number of elements 

#Without using set, saving space 
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        def backtrack(row_idx, col_idx,word_idx):
            if word_idx == len(word):
                return True
            if (row_idx<0 or row_idx>=rows or col_idx<0 or col_idx>=cols  or word[word_idx]!= board[row_idx][col_idx]):
                return False
            temp = board[row_idx][col_idx]
            board[row_idx][col_idx] = "#"
            res = (backtrack(row_idx+1, col_idx, word_idx+1) or
                  backtrack(row_idx-1, col_idx, word_idx+1) or
                  backtrack(row_idx, col_idx+1, word_idx+1) or 
                  backtrack(row_idx, col_idx -1, word_idx+1))
            board[row_idx][col_idx] = temp
            return res
        for row_idx in range(rows):
            for col_idx in range(cols):
                if backtrack(row_idx, col_idx, 0): return True
        return False
