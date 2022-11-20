# the idea is to build monotic increasing stack
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        print(num[:-2])
        for digit in num:
            while k>0 and stack and stack[-1]>digit:
                stack.pop()
                k-=1
            stack.append(digit)
        stack = stack[:-k] if k else stack
        res = "".join(stack)
        return str(int(res)) if res else "0"
        