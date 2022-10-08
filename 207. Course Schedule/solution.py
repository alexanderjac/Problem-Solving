class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        from collections import defaultdict
        def def_list():
            return list
        course_dict = defaultdict(def_list())
        for course , pre_req in prerequisites:
            course_dict[course].append(pre_req)
        path =[False for i in range(numCourses)]
        for course in range(numCourses):
            if self.dfs(course, course_dict, path):
                return False
        return True
    def dfs(self, course, course_dict, path):
        if path[course]:
            return True
        path[course] = True
        ret = False
        for child in course_dict[course]:
            ret =self.dfs(child, course_dict, path)
            if ret:break
        path[course] = False
        return ret

#Alternative Solution:
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        from collections import defaultdict
        def def_list():
            return list
        course_dict = defaultdict(def_list())
        for course , pre_req in prerequisites:
            course_dict[course].append(pre_req)
        for course in range(numCourses):
            path=set()
            if self.dfs(course, course_dict, path):
                return False
        return True
    def dfs(self, course, course_dict, path):
        if course in path:
            return True
        path.add(course)
        ret = False
        for child in course_dict[course]:
            ret =self.dfs(child, course_dict, path)
            if ret:break
        # after backtracking remove the course from the set
        path.remove(course)
        return ret

#TC: O(E+V) , where E is the number of dependencies, V is the number of courses and d is the maximum length of acyclic paths in the graph.
		# * First of all it would take E steps to build a graph in the first step.
		# * For a single round of backtracking, in the worst case where all the nodes chained up in a line, it would take us maximum V steps to terminate the backtracking.


# * Again, follow the worst case scenario where all the nodes are chained up in a line, it would take the following:
		#one node that is in the tail would take one time
		#second node before that node would process 2 node and so one
#so it would end up getting a time complexity of ∑V from 0 to V, which is V(V+1)/2
#As a result over all time complexity is O(E+V^2)

#SC: O(E+V)
	# * We built a graph data structures in the algorithm which would consume E+V space. 
` # * In addition, we employed a sort of bitmap (path) or set() to keep. track of all. visted nodes, which consumes V space.
  # * Finally since we implement the function in recursion, which would incur additional memory consumpption on call stack. In the worst case scenario all nodes are chained up in a line, the recursion would pile up V times
  # * Hence the overall space complexity of the algorithm would be O(E+ 3V) = O(E+V) 


#   Post Order DFS


#The rationale is that given a node, if the subgraph formed by all descendant nodes from this node has no cycle, then adding this node to the subgraph would not form a cycle either.

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        from collections import defaultdict
        course_dict = defaultdict(list)
        for course , prereq in prerequisites:
            course_dict[course].append(prereq)
        checked = set()
        path = set()
        for course in range(numCourses):
            if self.dfs(course, checked, path, course_dict ):
                return False
        return True
    def dfs(self, course, checked, path, course_dict):
        if course in checked :
            return
        if course in path:
            return True
        path.add(course)
        ret = False
        for child in course_dict[course]:
            ret = self.dfs(child, checked, path, course_dict)
            if ret: break
        path.remove(course)
        checked.add(course)
        return ret

# TC: O(E+V) where V is the number of courses, and E is the number of dependencies
  # * As in the previous algorithm, it would take us E time complexity to build a graph 
  # * Since we perform a postorder DFS traversal in the graph, we visit each vertex and each edge once and only once in the worst case, ie E+V

# SC: O(E+V) 
#Graph would consume E+V space.
#For both the path and checked set would consume 2*V space Finally, since we implement the function in recursion, which would incur additional memory consumption on call stack. In the worst case where all nodes chained up in a line, the recursion would pile up V times. Hence the overall space complexity of the algorithm would be O(E+4V) = O(E+V)

#Topological Sort
Explained https://www.cs.usfca.edu/~galles/visualization/TopoSortIndegree.html

from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:  
        #adjacency list 
        adjacency_list =defaultdict(list)
        #indegree counts the incoming edges
        indegree = [0]* numCourses
        for course , prereq  in prerequisites:
            adjacency_list[prereq].append(course)
            indegree[course]+=1
        #queue will contain the courses at that point which has indegree ==0
        queue = deque([])
        for i, value in enumerate(indegree):
            if value ==0:
                queue.append(i)
        topoSort =[]
        while queue:
            curr = queue.popleft()
            topoSort.append(curr)
            for neighbor in adjacency_list[curr]:
                indegree[neighbor]-=1
                if indegree[neighbor] ==0:
                    queue.append(neighbor)
        return len(topoSort) == numCourses

from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        degree = [0] * numCourses
        for (curr, pre) in prerequisite:
            adj[pre].append(curr)
            degree[curr] += 1
        queue = deque(i for (i, d) in enumerate(degree) if d == 0)
        visisted = 0
        while queue:
            curr = queue.popleft()
            visisted += 1
            for dep in adj[curr]:
                degree[dep] -= 1
                if not degree[dep]:
                    queue.append(dep)
        return visisted == numCourses
