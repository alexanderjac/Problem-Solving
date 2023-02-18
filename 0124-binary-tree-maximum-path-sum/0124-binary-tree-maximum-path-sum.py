# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def dfs(self, root): #15
    #     if not root: 
    #         return 0, 0
    #     LR, CLR = self.dfs(root.left) # 15,15
    #     RR, CRR= self.dfs(root.right) # 7, 7 
    #     currCValue = max(CLR, CRR) #   15
    #     currMax = max(LR+ root.val, RR+root.val) #35
    #     currCValue = max(root.val, LR+RR+root.val,currCValue )# 42
    #     # currCvalue = max(currCValue)
    #     return  currMax, currCValue  #35,42 
    def dfs(self, root):
        if not root:
            return 0
        leftSum = max( self.dfs(root.left),  0)
        rightSum = max(  self.dfs(root.right), 0)
        self.res = max(self.res, leftSum+rightSum+root.val)
        return max(leftSum, rightSum) + root.val
        
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = -float("inf")
        self.dfs(root)
        return self.res
        