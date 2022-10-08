# Below for loop based recursion doesnt have a return statement 
# it is because the return statement is not needed for loop based recursion 

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # for loop based backtracking recursion
        n = len(nums)
        res= []
        def helper (nums,curr ):
            res.append(curr)
            for i in range(len(nums)):
                helper(nums[i+1:], curr+[nums[i]])
        helper(nums, [])
        return res


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res= []
        
        def helper (curr, start, end_length):
            if len(curr) == end_length:
                res.append(curr[::])
                return
            
            for i in range(start,n):
                curr.append(nums[i])
                helper(curr,i+1, end_length)
                curr.pop()
        # return helper
    
        for k in range(n+1):
            helper([], 0, k)
            # print(res)
        return res
                
            
        
        
        
        # for loop based backtracking recursiomn
        
        # casacading
        casacading
        res =[[]]
        for num in nums:
            for i in range(len(res)):
                res +=[res[i]+[num]]
        return res

        # # backtracking solution
        n , res = len(nums), []
        def helper( temp, index):
            if index == n :
                res.append(temp.copy())
                return 
            temp.append(nums[index])
            helper( temp , index+1)
            if temp: temp.pop(-1)
            helper( temp ,index+1)
        helper( [],0 )
        return res