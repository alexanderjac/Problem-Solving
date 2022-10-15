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
            visited.add(current_node)
            if dist == k:
                result.append(current_node.val)    
#             process the current_node
            if current_node.left and dist<k and current_node.left not in visited:
                search_queue.append((current_node.left,dist+1) )
                # visited.add(current_node.left)
            if current_node.right and dist<k and current_node.right not in visited:
                search_queue.append((current_node.right, dist+1)  )
                # visited.add(current_node.right)
            if current_node in parent_hash and dist<k and parent_hash[current_node] not in visited:
                search_queue.append((parent_hash[current_node], dist+1)  )
                # visited.add(parent_hash[current_node])
            # visited.add(current_node)
        return result
            
            
            
            
            
        
    
        