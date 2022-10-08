class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        height = len(rooms)
        width = len(rooms[0])
        
        def dfs(ht, wt, dist):
            # base case
            if ht>= len(rooms) or ht<0 or wt <0 or wt>=len(rooms[0]) or rooms[ht][wt] < dist:
                return 
            rooms[ht][wt] = dist 
                
            dfs(ht+1, wt,  dist+1)
            dfs(ht, wt+1,  dist+1)
            dfs(ht-1, wt,  dist+1)
            dfs(ht, wt-1,  dist+1)
        for i in range(len(rooms)):
            for j in range(len(rooms[i])):
                if rooms[i][j] == 0:
                    dfs(i,j,0)


#DFS
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        height = len(rooms)
        width = len(rooms[0])
        queue =[]
        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] ==0:
                    queue.append((i, j))
        while queue:
            r, c = queue.pop(0)
            for dr , dc in ((1,0), (-1, 0), (0,1), (0,-1)):
                
                nr = r +dr
                nc = c+ dc
                if 0<=nr<len(rooms) and 0<=nc<len(rooms[0]) and rooms[nr][nc] ==2147483647:
                    rooms[nr][nc] = rooms[r][c] +1
                    queue.append((nr, nc))
        return rooms

# Think of reaching every empty cell as a race from the gate and each gate traversal will get there easily


import collections
def fill_distance_from_gate(rooms):
    m = len(rooms)
    n = len(rooms[0])
    INF = 2147483647
    neighbor = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def fill_distance(row, col):
        queue = collections.deque([(row, col)])
        distance = 1
        while queue:
            for _ in range(len(queue)):
                crow, ccol = queue.popleft() # current row, current col
                for nrow, ncol in neighbor:
                    nrow += crow
                    ncol += ccol
                    if m > nrow > -1 < ncol < n and rooms[nrow][ncol] > distance:
                        rooms[nrow][ncol] = distance
                        queue.append((nrow, ncol))
            distance += 1

    for row in range(m):
        for col in range(n):
            if not rooms[row][col]:
                fill_distance(row, col)

    return rooms
