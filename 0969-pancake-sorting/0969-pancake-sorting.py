class Solution:
    def flip(self,arr, k):
        start = 0 
        end = k -1
        while start<=end:
            arr[start], arr[end] = arr[end], arr[start]
            start +=1
            end -=1
        return arr
        
        
    def pancakeSort(self, A):
        result, n = [], len(A)
        for i in range(n,0,-1):
            
            pl = A.index(max(A[:i]))
            print(pl)
            if pl == i-1: continue
            if pl != 0:
                result.append(pl+1)
                A = self.flip(A, pl+1)
            result.append(i)
            self.flip(A, i)
            
        return result