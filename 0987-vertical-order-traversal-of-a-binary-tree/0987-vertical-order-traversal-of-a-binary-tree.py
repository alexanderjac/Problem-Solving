# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        hashMap = defaultdict(list)
        self.dfs(root, hashMap,0, 0 )
        # for i in range
        # result =[v for k, v in sorted(hashMap.items(), key=lambda item: item[0])]
        # print(hashMap)
        min_col =min(hashMap.keys())
        max_col =max(hashMap.keys())
        result =[]
        for col in range(min_col , max_col+1):
            temp =[]
            for j in sorted(hashMap[col]):
                temp.append(j[1])
            result.append(temp)
            
        return result
    def dfs(self, root ,hashMap, level,col):
        if not root:
            return

        hashMap[col].append((level,root.val))
        self.dfs(root.left, hashMap, level+1,col-1)
        self.dfs(root.right, hashMap, level+1, col+1)
        