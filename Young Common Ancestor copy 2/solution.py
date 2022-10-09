# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

TC: O(n)
SC: O(n)
class Solution(object):
    def distanceK(self, root, target, k):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type k: int
        :rtype: List[int]
        """
        
        #Step 1: Make graph adjacency list using hash:
        #{3:[5,1], 5:[3,1,6,2], 1:[0,8,3]}...
        #Append nodes for both parent and child
        
        d = defaultdict(set)
        def dfs(root, d):
            if root.right:
                d[root.val].add(root.right.val)
                d[root.right.val].add(root.val)
                dfs(root.right, d)
            if root.left:
                d[root.val].add(root.left.val)
                d[root.left.val].add(root.val)
                dfs(root.left, d)
        dfs(root,d)
        
        #Step 2: Traverse BFS starting from target
        #Store distance as well
		
        q = [(target.val,0)]
        v = {target.val} #visited
        res = []
        while(q):
            cur, dist = q.pop()
            if (dist == k): res.append(cur)
            for i in list(d[cur]):
                if i in v: continue
                v.add(i)
                q.append((i,dist+1))
        return res



# Solution 2
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        result =[]
        parent_hash = {}
        queue = [root]
        while queue:
            curr_node = queue.pop(0)
            if curr_node.left:
                queue.append(curr_node.left)
                parent_hash[curr_node.left] = curr_node
            if curr_node.right:
                queue.append(curr_node.right)
                parent_hash[curr_node.right] = curr_node
        search_queue = [(target,0)]
        visited = set()
        visited.add(target)
        while search_queue:
            current_node, dist = search_queue.pop(0)
            if dist == k:
                result.append(current_node.val)    
#             process the current_node
            if current_node.left and dist<k and current_node.left not in visited:
                search_queue.append((current_node.left,dist+1) )
                visited.add(current_node.left)
            if current_node.right and dist<k and current_node.right not in visited:
                search_queue.append((current_node.right, dist+1)  )
                visited.add(current_node.right)
            if current_node in parent_hash and dist<k and parent_hash[current_node] not in visited:
                search_queue.append((parent_hash[current_node], dist+1)  )
                visited.add(parent_hash[current_node])
            # visited.add(current_node)
        return result