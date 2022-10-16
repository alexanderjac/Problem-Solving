class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = []
        height = len(grid)
        width = len(grid[0])
        count_1 =0
        for i in range(height):
            for j in range(width):
                if grid[i][j] ==2:
                    queue.append((i, j))
                elif grid[i][j] ==1:
                    count_1 +=1
        if count_1 == 0:
            return 0
        count = 0
        while queue:
            for i in range(len(queue)):
                r, c  = queue.pop(0)
                for dr, dc in ((0,1),(1,0), (0,-1), (-1,0)):
                    row = r+dr
                    col = c +dc
                    if  row>=0 and row<height and col>=0 and col<width and grid[row][col] ==1 :
                        print((row,col))
                        grid[row][col] = 2
                        queue.append((row, col))
            count +=1
        for i in range(height):
            for j in range(width):
                if grid[i][j] ==1:
                    return -1
            
        return count -1
                        
        