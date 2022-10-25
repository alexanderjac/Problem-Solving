class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = [( -(self.squarefunc(points[i])), i) for i in range(k)]
        heapq.heapify(heap)
        for i in range(k, len(points)):
            dist = -self.squarefunc(points[i])
            if dist>heap[0][0]:
#               got this above line?  
                heapq.heappushpop(heap, (dist, i))
        return [points[i] for _, i in heap]
        
    def squarefunc(self, point):
        return point[0]**2 + point[1]**2
        