#DFS Recursively 
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        oldToNew ={}
        def dfs(node):
            if not node:
                return
            node_copy = Node(node.val, [])
            oldToNew[node] = node_copy
            for neighbor in node.neighbors:
                if neighbor in oldToNew:
					node_copy.neighbors.append(oldToNew[neighbor])
                else:
					node_copy.neighbors.append(dfs(neighbor))
            return node_copy
        return dfs(node)

Alternative solution:
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        oldToNew = {}
        def dfs(node):
            if not node:
                return
            if node in oldToNew:
                return oldToNew[node]
            clone_node = Node(node.val, [])
            oldToNew[node] =clone_node
            if node.neighbors:
                clone_node.neighbors = [dfs(neighbor) for neighbor in node.neighbors ]
            return clone_node
        return dfs(node)

TC: O(N+M) , N is the number of edges and M is the number of vertices
SC: O(N) , This space is occupied by the visited hash map and in addition to that, space would be occupied by the recursive stack since we are adopting a recursive approach here. The space occupied by the recursion stack would be equal to O(H) where H is the height of the graph. Overall the space would be O(N)

#DFS iteratively
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        stack =[node]
        oldToNew = {}
        clone = Node(node.val, [])
        oldToNew[node] = clone
        while stack:
            node = stack.pop()
            for neighbor in node.neighbors:
                if neighbor not in oldToNew:
                    clone_node = Node(neighbor.val,[])
                    oldToNew[neighbor] = clone_node
                    oldToNew[node].neighbors.append(oldToNew[neighbor])
                    stack.append(neighbor)
                else:
                    oldToNew[node].neighbors.append(oldToNew[neighbor])
        return clone
#DFS iteratively clean Code -->
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return 
        stack =[node]
        oldToNew = {}
        clone = Node(node.val, [])
        oldToNew[node] = clone
        while stack:
            node = stack.pop()
            # print(node.val)
            for neighbor in node.neighbors:
                if neighbor not in oldToNew:
                    oldToNew[neighbor] = Node(neighbor.val,[])
                    stack.append(neighbor)
                oldToNew[node].neighbors.append(oldToNew[neighbor])
        return clone
#BFS using a stack
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return 
        stack =deque([node])
        oldToNew = {}
        clone = Node(node.val, [])
        oldToNew[node] = clone
        while stack:
            node = stack.popleft()
            # print(node.val)
            for neighbor in node.neighbors:
                if neighbor not in oldToNew:
                    oldToNew[neighbor] = Node(neighbor.val,[])
                    stack.append(neighbor)
                oldToNew[node].neighbors.append(oldToNew[neighbor])
        return clone

