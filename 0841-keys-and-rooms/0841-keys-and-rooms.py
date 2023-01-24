class Solution:
    from collections import defaultdict 
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        adjList = rooms
        visited = set()
        def dfs(node, parent ): #3, 0
            if node not in visited:
                visited.add(node)  # 0 , 1 
                for children in adjList[node]:  #   0 , 1
                    dfs(children, node )
        dfs(0, -1)
        return len(visited) == len(rooms)