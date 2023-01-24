class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        posCol = set()
        negCol = set()
        board = [["."]*n for i in range(n)]
        result = []
        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                result.append(copy)
                return
            for c in range(n):
                if c in col or (r+c) in posCol or (r-c) in negCol:
                    continue
                col.add(c)
                posCol.add(r+c) #why adding r-c and not (r,c)? - because if r-c is there it means that diagonal is visited
                negCol.add(r-c)
                board[r][c] ="Q"
                backtrack(r+1)
                col.remove(c)
                posCol.remove(r+c)
                negCol.remove(r-c)
                board[r][c] ="."
        backtrack(0)
        return result                
        