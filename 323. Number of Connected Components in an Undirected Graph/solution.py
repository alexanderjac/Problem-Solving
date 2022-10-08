class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # adjacency list
        visited =defaultdict(list)
        # seen set while traversing
        seen = set()
        counter =0
        # creating adjacency list 
        for edge in edges:
            start , end = edge[0] , edge[1]
            visited[start].append(end)
            visited[end].append(start)
        # for nodes that are connected wont be part of the edges list 
        for i in range(n):
            if i not in visited:
                counter+=1    
        def dfs (node):
            if node in seen:
                return
            seen.add(node)
            for neighbor in visited[node]:
                dfs(neighbor)
        # calling all edges 
        for edge in edges:
            if not edge[0] in seen:
                dfs(edge[0])
                counter+=1
        return counter
TC : O(E+V), since its visiting all edges and vertices
SC: O(E+V) Building the adjacency list will take O(E) space. To keep track of visited vertices, an array of size O(V) is required. Also, the run-time stack for DFS will use O(V){O}(V)O(V) space.