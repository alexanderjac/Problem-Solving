class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack =[["$", 0]]
        for c in s:
            if stack[-1][0] == c:
                stack[-1][1] +=1
                if stack[-1][1] == k:
                    stack.pop(-1)
            else:
                stack.append([c, 1])
        return ''.join( c*count for c, count in stack)
        # stack = []
        # for i in range(len(s)):
        #     stack.append(s[i])
        #     print
        #     if len(stack) >=k:
        #         char = stack[-1]
        #         dupl = True
        #         for j in range(len(stack)-1, len(stack)-k-1, -1):
        #             if stack[j] != char:
        #                 dupl = False
        #         if dupl:
        #             for _ in range(k):
        #                 stack.pop(-1)
        #             print(i, stack)
        # result = ""
        # for i in range(len(stack)):
        #     result+=stack[i]
        # return result