class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        """
        [10,20],[30,200],[400,50],[30,20]
         10(a)    30(a)     50(a)    20(a)
            
          10        170     -350    -10
        
        [[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]
         259(a)    54(a)    667(a)    184(a)    118(a)     577(a)   
         511        -394        -259      -45      -722      -108
            
        """
        heap =[]
        heapq.heapify(heap)
        length=  len(costs)
        result =0
        for a,b in costs:
            heapq.heappush(heap, (b-a) )
            result +=a
        # cost_final = [ a for a, _ in costs ]
        counter =0
        # result = sum(cost_final)
        while counter <length//2:
            ele  = heapq.heappop(heap)
            result +=ele
            counter +=1
        return result
            
        
        