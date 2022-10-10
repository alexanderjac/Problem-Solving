# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # inorder traversal ; fun fact: inorder traversal list would be sorted
        result =[]
        self.inorder(root, result)
        for i in range(1,len(result)):
            if result[i-1]>= result[i]:
                return False
        return True
        
    def inorder(self, node, result):
        if not node:
            return 
        self.inorder(node.left, result)
        result.append(node.val)
        self.inorder(node.right, result)
        
        
        
        # dfs
#         def valid(node, left, right):
#             if node == None:
#                 return True
#             if node.val<= left or node.val>=right:
#                 return False
#             return (valid(node.left, left, node.val) and valid(node.right, node.val, right))
            
#         return (valid(root, float(-inf), float(inf)))
                
            
#         if root == None:
#             return True
#         if root.left and root.right:
#             if root.left.val>= root.val or root.right.val <=root.val:
#                 return False
#         else:
#             return True
#         return self.isValidBST(root.left) and self.isValidBST(root.right)

        
        