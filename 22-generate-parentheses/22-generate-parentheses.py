class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result=[]
        self.backtrack("",n, result)
        return result
        
    def backtrack(self,string ,n, result):
        
        if len(string) == 2*n:
            stack =[]
            for char in string:
                if stack and char ==")" and stack[-1] == "(":
                    stack.pop(-1)  
                else: 
                    stack.append(char)
            if not stack:
                result.append(string)
            return 
        self.backtrack(string+"(",n, result)
        self.backtrack(string+ ")",n, result)
        
            