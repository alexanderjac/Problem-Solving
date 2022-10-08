#bfs solutiom
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        count =0
        visited = set()
        rows, cols = len(grid), len(grid[0])
        def bfs(r, c):
                q = collections.deque()
                visited.add((r, c))
                q.append((r, c))
                while q:
                    row, col = q.popleft()
                    directions = [[1,0], [-1,0],[0,1],[0,-1]]
                    for dr, dc in directions:
                        r = row+dr
                        c= col+dc
                        if (0<=r <rows and 0<=c <cols and grid[r][c] =='1' and (r, c) not in visited) :
                            # grid[r][c ]='0'
                            q.append((r, c))
                            visited.add((r,c))        
        for row_idx in range(rows):
            for col_idx in range(cols):
                if grid[row_idx][col_idx] == '1' and (row_idx, col_idx) not in visited :
                    # grid[row_idx][col_idx]='0'
                    bfs(row_idx, col_idx)
                    count+=1
        return count
# TC:O(M*N)
# M is the number of rows and N is the number of columns
# SC:O(min(M,N)) because in worst case where the grid is filled with lands, the size of queue can grow up to min(M,NM,N).

#dfs solution
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count =0
        rows, cols = len(grid), len(grid[0])
        for row_idx in range(rows):
            for col_idx in range(cols):
                if grid[row_idx][col_idx] == "1":
                    self.dfs(row_idx, col_idx, grid)
                    count+=1
        return count
    def dfs (self, row, col, grid):
        if row<0 or col<0 or row>=len(grid) or col>= len(grid[0]) or grid[row][col]!= "1":
            return
        grid[row][col] ="#"
        self.dfs(row+1, col, grid)
        self.dfs(row-1, col, grid)
        self.dfs(row, col+1, grid)
        self.dfs(row, col-1, grid)

# TC:O(M*N)
# M is the number of rows and N is the number of columns
# SC:worst case O(M*N) in case that the grid map is filled with lands where DFS goes by M*N deep
