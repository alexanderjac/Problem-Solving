class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # for loop based backtrack
        
#         def backtrack(curr, start):
#             if sum(curr)>= target or start>= n:
#                 if sum(curr) == target :
#                     res.append(curr[:])
#                 return
#             for i in range(start,n):
#                 # curr+=[candidates[i]]
#                 backtrack(curr + [candidates[i]], i)
#                 # curr.pop(-1)
#         res = []
#         n = len(candidates)
#         backtrack([], 0)
#         return res
        
            
        
        # backtrack using recursion
        def helper(curr, index):
            if sum(curr) >=target or index>=n:
                if sum(curr) == target :
                    res.append(curr[::])
                return
            helper(curr, index+1)
            curr += [candidates[index]]
            helper(curr, index)
            if curr: curr.pop(-1)
            
        n =len(candidates)
        res =[]
        helper(curr = [], index =0)
        return res
        