#Topological Sort
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        indegree = [0 for i in range(numCourses)]
        for course, pre in prerequisites:
                    adj[pre].append(course)
                    indegree[course]+=1
        queue =deque([])
        for course, value in enumerate(indegree):
                    if value == 0:
                        queue.append(course)
        result = []
        while queue:
                    curr = queue.popleft()
                    result.append(curr)
                    for course in adj[curr]:
                            indegree[course]-=1
                            if indegree[course] == 0:
                                queue.append(course)
        if len(result) == numCourses:
            return result
        else: return []

TC: O(V+E) where V represents the number of courses and E represents the number of Edges. We pop each node exactly once from the zero in-degree queue and that gives us V. Also, for each vertex, we iterate over its adjacency list and in totality we iterate through all edges in totality gives E. Hence O(V+E)
SC: O(V+E) We use an intermediate queue data structure to keep all the nodes with 0 in-degree. In the worst case, there wont be any prerequisite relationship abnd the qeueu would contain all the nodes since all are 0 in-degree. That gives us O(V). Additionally  we also use adjacency list to represent graph initially. The space occupied is defined by the number of edges because for each node as the key, we have all its adjacency list node in the form of a list as the value. Hence O(E). So the overall space complexity would be O(V+E)