class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:        
        if not heights or not heights[0]:
            return []
        rows = len(heights)
        cols = len(heights[0])
        pac_queue =deque()
        atl_queue = deque()
        for i in range(cols):
            pac_queue.append((0,i))
            atl_queue.append((rows-1, i))
        for i in range(rows):
            pac_queue.append((i,0))
            atl_queue.append((i, cols-1))
        def bfs(queue):
            result = set()
            visited = set()
            while queue:
                row, col = queue.popleft()
                result.add((row, col))  
                for dr, dc in [[0,1], [0,-1],[1,0],[-1,0]]:
                    dr = row+dr
                    dc = dc+col
                    if dr in range(rows) and dc in range(cols) and heights[dr][dc]>= heights[row][col] and (dr, dc) not in result:
                        queue.append(((dr, dc)))
            return result
        pac_set = bfs(pac_queue)
        atl_set = bfs(atl_queue)
        return list(pac_set& atl_set)

#TC: O(M*N) where M is the number of rows and N is the number of columns
#In the worst case, such as a matrix where every value is equal, we would visit every cell twice. This is because we do two traversal and during each traversal we visit each cell exactly once. There ara M*N cells which arises a tc: O(2*M*
#N) =O(M*N)
#SC: O(M*N) The extra space we use comes from our queues, and the data structurewe use to keep track of what cells have been visited. Similar to the time complexity, for a given ocean, the amount of space we will use scales linearly with the number of cells. For example, in the Java implementation, to keep track of what cells have been visited, we simply used 2 matrices that have the same dimensions as the input matrix. The same logic follows for the queues - we can't have more cells in the queue than there are cells in the matrix!



#DFS Solution
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:        
        if not heights or not heights[0]:
            return []
        rows = len(heights)
        cols = len(heights[0])
        pac = set()
        atl = set()
        def dfs(row, col, res):
            # if  (row,col) in res:
            #     return 
            res.add((row,col))
            for dr , dc in [[0,1], [0,-1], [-1,0], [1,0]]:
                dr = row +dr
                dc = col +dc
                if dr not in range(rows) or dc not in range(cols):
                    continue
                if heights[dr][dc]<heights[row][col]:
                    continue
                if (dr, dc) in res:
                    continue
                dfs(dr, dc, res)
#both can work
            # if row+1 in range(rows) and col in range(cols) and heights[row+1][col]>= heights[row][col]:dfs(row+1, col,res)
            # if row-1 in range(rows) and col in range(cols) and heights[row-1][col]>= heights[row][col]:dfs(row-1, col, res)
            # if row in range(rows) and col-1 in range(cols) and heights[row][col-1]>= heights[row][col]:dfs(row, col-1, res)
            # if row in range(rows) and col+1 in range(cols) and heights[row][col+1]>= heights[row][col]:dfs(row, col+1, res)
            
            
        for i in range(cols):
            # pacific
            dfs(0, i, pac)
            # atlatntic
            dfs(rows-1, i, atl)
        for i in range(rows):
            # pacific
            dfs(i, 0, pac)
            # atlatinc
            dfs(i, cols-1, atl)
        return pac.intersection(atl)

#TC: O(M*N) where M is the number of rows and N is the number of columns. Similar to approach 1. The dfs function runs exactly once for each cell accessible from an ocean.
#SC: O(M*N) Similar to approach 1. Space that was used by our queues is now occupied by dfs calls on the recursion stack.