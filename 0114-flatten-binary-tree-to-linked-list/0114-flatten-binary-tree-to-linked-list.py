# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root == None:
            return None
        head = root
        while root :
            if root.left:
                curr = root.left
                while curr.right:
                    curr = curr.right
         
                # if curr.right == None :
                curr.right = root.right
                root.right = root.left
                root.left  = None
            root = root.right
                    
                    
                    
                    
        """
                    while node:
        if node.left:
            pre=node.left
            while pre.right:
                pre=pre.right
            pre.right=node.right
            node.right=node.left
            node.left=None
        node=node.right
        """