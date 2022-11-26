from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:  
        rowsize = len(grid)
        colsize = len(grid[0])
        if grid[0][0] or grid[rowsize-1][colsize-1]:
            return -1
        queue = deque([(0, 0, 1)])
        # visited = set()
        grid[0][0] =1
        while queue:
            r, c, d = queue.popleft()
            if r == rowsize -1 and c== colsize-1:
                return d
            # visited.add((r,c))
            for dr, dc in ((0,1), (1,0), (0,-1), (-1,0),(1,1), (-1,1), (1,-1),(-1,-1)):
                row = r+dr
                col = c+dc
                if 0<=row<rowsize and 0<=col<colsize and grid[row][col] == 0 :

                    grid[row][col] =1
                    queue.append((row, col,d+1))
        return -1

#     def shortestPathBinaryMatrix(self,grid):
#         n = len(grid)
#         if grid[0][0] or grid[n-1][n-1]:
#             return -1
#         q = [(0, 0, 1)]
#         grid[0][0] = 1
#         for i, j, d in q:
#             if i == n-1 and j == n-1: return d
#             for x, y in ((i-1,j-1),(i-1,j),(i-1,j+1),(i,j-1),(i,j+1),(i+1,j-1),(i+1,j),(i+1,j+1)):
#                 if 0 <= x < n and 0 <= y < n and not grid[x][y]:
#                     grid[x][y] = 1
#                     q.append((x, y, d+1))
#         return -1

