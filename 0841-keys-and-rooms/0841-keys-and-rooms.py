class Solution:
    from collections import defaultdict 
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        adjList = rooms
        # for roomNumber, keys in enumerate(rooms):
        #     for key in keys:
        #         adjList[roomNumber].add(key)
                # adjList[key].add(roomNumber)
        visited = set()
        def dfs(node, parent ): #3, 0
            # base case 
            if node in visited:
                return   
            visited.add(node)  # 0 , 1 
            # if len(adjList[node]) ==0:
            #     return False 
            for children in adjList[node]:  #   0 , 1
                if children != parent  : 
                    dfs(children, node )
                           
            return  
        
        dfs(0, -1)
        print(visited) 
        return   len(visited) == len(rooms)
            
                
        """
        [[1,2],[2,1],[1]]
        
        0: 1, 2
        1: 2
        2: 1
        
        
          0   1   2   3
        [[1],[2],[3],[]]
          0      1      2   3
        [[1,3],[3,0,1],[2],[0]]
          0 - > 1 -> 3 
        
        Graph valid Tree
        
        0: 1, 3 
        1: 3, 0, 1
        2: 2
        3 : 0, 1
        
       len( set()) == n 
        
        
        
        """
        