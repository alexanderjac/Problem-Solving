# backtracking with for loop and popping
def dfs(nums, path):
            if not nums:
                res.append(path.copy())
                return
            for i in range(len(nums)):
                path+=[nums[i]]
                dfs(nums[:i]+nums[i+1:], path)
                path.pop(-1)
                
        res =[]
        dfs(nums, [])

# recursive without backtracking solution
def permute(self, nums: List[int]) -> List[List[int]]:
        
        def dfs(nums, path):
            if not nums:
                res.append(path)
                return
            for i in range(len(nums)):
                dfs(nums[:i]+nums[i+1:], path+[nums[i]])
                
        res =[]
        dfs(nums, [])
        return res
"""

## **Approach 1: Recursive with backtracking (implicit stack)**

---

**Big-O:**

- 
    
    **Time:** `O(N*N!)`
    
    - 
        
        **Why O(N*N!) and not just O(N!) ?**Many people are debating in the solution tab whether time-complexity should be `O(N!)` or `O(N * N!)`. Below are two intuitive arguments as to why it should be `O(N*N!)`. Let's forget for a while about the recursive nature of the algorithm and examine the **N-ary, recursive, space-tree** that is generated by the recursive algorithm.
        
        ![https://assets.leetcode.com/users/images/ac9c35dc-89b8-4860-b08c-d2f60859e43e_1609289801.6830964.png](https://assets.leetcode.com/users/images/ac9c35dc-89b8-4860-b08c-d2f60859e43e_1609289801.6830964.png)
        
    1. In order to reaverse the tree, will visit each node once, we know very well that would cost us `O(N)` in a binary tree and `O(E+V)` in an N-ary tree where V = vertices and E = edges (or number of children). Now for the [1,2,3] example shown in the sketch, we can see there is a total of 16 nodes/verticies and that |E| varies from level to level with an upper limit of N and a lower limit of 1.
        - So, we can say roughly O(E+V) = a little more than 16
        - O(N!) on the other hand = 6
        - whereas, O(N*N!) = 3*6 = 18
    2. Another way of looking at is we know from set theory that there are N! permutations of a list of size N. We also know that the permutations are going to be the leaves of the tree, which means we will have N! leaves. In order to get to each one of those leaves, we had to go through N calls. That's O(N*N!). Again a little more than the total number of nodes because some nodes are shared among more than one path.

**Space:** `O(N!)`

- Because you still need to store the permutations and there are N! of them even if the depth of the stack is maxed out at N+1 (depth of the recursion space-tree is also N+1). See figure below.

**Code:**

```python
def permute(self, nums):
	# helper
	def recursive(nums, perm=[], res=[]):
		if not nums: # -- NOTE [1]
			res.append(perm[::]) #  -- NOTE [2] - append a copy of the perm at the leaf before we start popping/backtracking

		for i in range(len(nums)): # [1,2,3]
			newNums = nums[:i] + nums[i+1:]
			perm.append(nums[i])
			recursive(newNums, perm, res) # - recursive call will make sure I reach the leaf
			perm.pop() # -- NOTE [3]
		return res

return recursive(nums)

# NOTE [1]:
# --------
# nums is empty at the leaf of the recursive tree

# NOTE [2]:
# --------
# at the leaf -> we know we have exaushted one path/permutation (each path is a permutation in a recursive tree)
# reason why we are copying here is because at lists are passed by reference and since we are maintaining only one path/perm variable throughput, we are gonna be modifiying that path variable (popping it to be precise) in order to revert the path to a previous state (aka parent node) in preperation to make a lateral/horizontal move to a sibling node. See explanation below for further understanding.

# NOTE [3]:
# ---------
# See below

```

**NOTE [3] Explained further : Why do we need to backtrack?**

- Notice how in the code above, there is only one variable path (or perm) throughout the problem. This variable is passed to one recursive call after another recursive call as we move from the input (the root of the tree) to the leaf (the permutation) and obviously it gets modified multiple times along the way. As we keep building the path (or perm). It goes from `> [1,2] -> [1,2,3]` as you can see in the left-most branch. However, what actually happens is that everytime we append a number to the path, **we are actively changing the path from previous recursive states as well**, since all of these point to the same path list and are not independent states/copies. Since effectively all these aliases are pointing to the same memory location, any change to the variable are echoed to all of its aliases. This can be problematic because it alters the the previous states. See below for visual illustration of the problem.

![https://assets.leetcode.com/users/images/2dad4626-ba5b-4d8f-adcb-90249a1eddb4_1609299083.319523.png](https://assets.leetcode.com/users/images/2dad4626-ba5b-4d8f-adcb-90249a1eddb4_1609299083.319523.png)

- To overcome this problem, we need to backtrack. It's tempting to think backtracking is needed only in situations where we encounter an obstacle while building/searching for the solution (such as hitting a wall while traversing a maze), however, backtracking as a technique has broader scope than just that. Any situation where we might need to access a previous state of a variable that keeps changing during the execution of the program requires backtracking. As mentioned earlier an coming across an obstacle in a maze (or anything that renders the path being explored invalid) is NOT the only incident backtracking is called upon. Backtracking would still be required even if the current path being explored is valid, in order to explore the next path. Think of a parent node from which two child nodes diverge. After exploring the first child, we need to backtrack to parent to investigate the sibling node (other child). This situation takes place in our space-tree. See sketch below.

![https://assets.leetcode.com/users/images/ea5e3934-308b-486b-bd9d-ba5d84972c93_1609311308.955607.png](https://assets.leetcode.com/users/images/ea5e3934-308b-486b-bd9d-ba5d84972c93_1609311308.955607.png)

- 
    
    As you can see in the sketch above, by the time we reach node B, the path = [1,2,3]. These changes are echoed up to the parent node and even all the way up to the root if we don't backtrack which will ruin subsequent paths (ex: ParentNode -> node C) is missed up. This can be alleviated by popping the path after each recursive call as we did in our code.
    
    ```
    for i in range(len(nums)): # [1,2,3]
    	newNums = nums[:i] + nums[i+1:]
    	perm.append(nums[i])
    	recursive(newNums, perm, res)
    	perm.pop() # -- BACKTRACK
    
    ```
    
- The recursive algorithm above produces a chain of nodes (no branching):
    
    It's also worth-mentioning that backtracking was needed here because of the branching nature of the space-tree. Backtracking won't be required if the recursive algorithm produces a linked-list rather than a space-tree. An example of such algorithm is recursively summing up numbers from 0 -> N
    
    ```
    def sumPosNumLessThanN(N, res=0):
    	if N == 0:
    		return res
    	else:
    		res = 1 + sumPosNumLessThanN(N-1)
    	return res
    
    ```
    
    ![https://assets.leetcode.com/users/images/65a431a3-c09d-4926-b431-8df5eb2a4cf3_1609312872.9623408.png](https://assets.leetcode.com/users/images/65a431a3-c09d-4926-b431-8df5eb2a4cf3_1609312872.9623408.png)
    

**NOTE [2] Explained further : Why do we need to copy?**

- You probably have guessed it by now. As shown above, due to the constantly changing state of our data/variables, we need to append a copy of the path `res.append(path[::])` at the leaf, instead of appending the path itself. The reason being that lists are mutable and are passed by reference, so even after appending a path to our result list, that path will still be affected by any changes to its aliases (will be afftected by all the poppping and backtracking taking place) and by the time our recursion calls make their way to the top/root, the path will be empty `path = [ ]`

**Backtracking seems like a pain in the a$$. Is there a way around it?**

- Glad you asked, yes, there is! We can avoid backtracking all together with a little bit of book-keeping. Instead of having to backtrack to revert to a previous state of the data/variables, we could save snapshots of the data/variables at each step along the way so that we never have to manually backtrack. This can be done either recursively or iteratively by passing a copy of our data. See Approach 2 for recursive without backtracking, and Approach 3 for an itertaive solution without backtracking below..

## **Appraoch 2: Recursive without backtracking (implicit stack)**

---

**Big-O:**

- Time: `O(N*N!)`
- Space: `O(N!)`

**Code:**

```
def recursive(nums, perm=[], res=[]):

            if not nums:
                res.append(perm) # --- no need to copy as we are not popping/backtracking. Instead we're passing a new variable each time

            for i in range(len(nums)):
                newNums = nums[:i] + nums[i+1:]
                # perm.append(nums[i]) # --- instead of appending to the same variable
                newPerm = perm + [nums[i]] # --- new copy of the data/variable
                recursive(newNums, newPerm, res)
                # perm.pop()  # --- no need to backtrack
            return res

        return recursive(nums)

```

**How backtracking was avoided? Approach 2 vs. Approach 3**

- Below is a comparison between the two approaches. Notice how on the left side, only one `perm/path` variable is maintained throughout as opposed to multiple `perm/path` snapshots at each step on the right hand side.

![https://assets.leetcode.com/users/images/0a74e098-5a23-4859-8518-2ffe513ea965_1609340194.1382449.png](https://assets.leetcode.com/users/images/0a74e098-5a23-4859-8518-2ffe513ea965_1609340194.1382449.png)

- Illustartions above are generated using this [Python Tutor tool](http://www.pythontutor.com/visualize.html#mode=edit)
    - Approach 2 : Recursive w backtracking : [here](http://www.pythontutor.com/visualize.html#code=def%20recursivePermute%28nums,%20perm%3D%5B%5D,%20res%3D%5B%5D%29%3A%0A%20%20%20%20if%20not%20nums%3A%20%0A%20%20%20%20%20%20%20%20res.append%28perm%29%20%0A%20%20%20%20%0A%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20for%20i%20in%20range%28len%28nums%29%29%3A%20%23%20%5B1,2,3%5D%0A%20%20%20%20%20%20%20%20%20%20%20%20newNums%20%3D%20nums%5B%3Ai%5D%20%2B%20nums%5Bi%2B1%3A%5D%0A%20%20%20%20%20%20%20%20%20%20%20%20perm.append%28nums%5Bi%5D%29%0A%20%20%20%20%20%20%20%20%20%20%20%20recursivePermute%28newNums,%20perm,%20res%29%20%23%20-%20recursive%20call%20will%20make%20sure%20I%20reach%20the%20leaf%0A%20%20%20%20%20%20%20%20%20%20%20%20perm.pop%28%29%20%0A%0A%20%20%20%20return%20res%0A%0Aprint%28recursivePermute%28%5B1,2,3%5D%29%29&cumulative=false&curInstr=25&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)
    - Approach 3: Recursive w/o backtracking : [here](http://www.pythontutor.com/visualize.html#code=def%20recursivePermute%28nums,%20perm%3D%5B%5D,%20res%3D%5B%5D%29%3A%0A%20%20%20%20if%20not%20nums%3A%20%0A%20%20%20%20%20%20%20%20res.append%28perm%5B%3A%3A%5D%29%20%0A%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20for%20i%20in%20range%28len%28nums%29%29%3A%20%23%20%5B1,2,3%5D%0A%20%20%20%20%20%20%20%20%20%20%20%20newNums%20%3D%20nums%5B%3Ai%5D%20%2B%20nums%5Bi%2B1%3A%5D%0A%20%20%20%20%20%20%20%20%20%20%20%20newPerm%20%3D%20perm%20%2B%20%5Bnums%5Bi%5D%5D%0A%20%20%20%20%20%20%20%20%20%20%20%20recursivePermute%28newNums,%20newPerm,%20res%29%20%23%20-%20recursive%20call%20will%20make%20sure%20I%20reach%20the%20leaf%0A%0A%20%20%20%20return%20res%0A%0Aprint%28recursivePermute%28%5B1,2,3%5D%29%29&cumulative=false&curInstr=23&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)..

---

## **Approach 3 : DFS Iterative with Explicit Stack**

---

**Big-O:**

- Time: `O(E+V)` which is the same as => `O(N*N!)`
- Space: `O(N!)`

**Code:**

```
def recursive(nums):
	 stack = [(nums, [])]   # -- nums, path (or perms)
	 res = []
	 while stack:
		 nums, path = stack.pop()
		 if not nums:
			 res.append(path)
		 for i in range(len(nums)):   # -- NOTE [4]
			 newNums = nums[:i] + nums[i+1:]
			 stack.append((newNums, path+[nums[i]]))  # --  just like we used to do (path + [node.val]) in tree traversal
	 return res

# NOTE [4]
# The difference between itertaive tree/graph traversal we did before and this one is that
# in most tree/graph traversals we are given the DS (tree/graph/edges) whereas here we have to build the nodes before we # traverse them
# Generating the nodes is very simple, we Each node will be (nums, pathSofar)

```

## **..**

## **Approach 4 : BFS Iterative with a queue**

---

**Big-O:**

- Time: `O(E+V)` which is the same as => `O(N*N!)`
- Space: `O(N!)`

**Code:**

```
def recursive(nums):
	from collections import deque
	q = deque()
	q.append((nums, []))  # -- nums, path (or perms)
	res = []
	while q:
		nums, path = q.popleft()
		if not nums:
			res.append(path)
		for i in range(len(nums)):
			newNums = nums[:i] + nums[i+1:]
			q.append((newNums, path+[nums[i]]))
	return res

```

- **For JAVA implementation of all 4 approaches : checkout this post** => [https://leetcode.com/problems/permutations/discuss/996115/Java-4-Approaches-Visuals-%2B-Time-Complexity-Analysis](https://leetcode.com/problems/permutations/discuss/996115/Java-4-Approaches-Visuals-%2B-Time-Complexity-Analysis)
"""