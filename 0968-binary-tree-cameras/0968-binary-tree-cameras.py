# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def dfs(node):
            if not node:
                return False, True
            c1,m1 = dfs(node.left)
            c2,m2 = dfs(node.right)
            camera, monitor = False, False
            if c1 or c2:
                monitor = True
            if not m1 or not m2:
                camera = True
                self.res +=1
                monitor = True
            return camera, monitor
        c, m = dfs(root)
        if not m:return self.res +1
        return self.res