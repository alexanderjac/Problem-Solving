# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self, root, array):
        if root == None:
            return
        
        array.append(root)
        if root.left:
            self.inorder(root.left, array)
            root.left = None
        if root.right:
            self.inorder(root.right, array)
            root.right = None
        
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root == None:
            return None
        array = []
        self.inorder(root, array)
        head = array[0]
        for i in range(1, len(array)):
            head.right = array[i]
            head = head.right
        return head