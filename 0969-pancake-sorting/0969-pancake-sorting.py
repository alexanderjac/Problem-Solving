class Solution:
    def pancakeSort(self, A):
        result, n = [], len(A)
        for i in range(n,0,-1):
            
            pl = A.index(max(A[:i]))
            print(pl)
            if pl == i-1: continue
            if pl != 0:
                result.append(pl+1)
                A[:pl+1] = A[:pl+1][::-1]
            result.append(i)
            A[:i] = A[:i][::-1]
            
        return result