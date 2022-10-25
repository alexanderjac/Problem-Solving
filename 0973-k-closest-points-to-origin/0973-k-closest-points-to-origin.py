class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # # sol3 with optimized heap approach
        # heap = [(-(self.squarefunc(points[i])), i) for i in range(k)]
        # heapq.heapify(heap)
        # for i in range(k, len(points)):
        #     dist = -self.squarefunc(points[i])
        #     if dist>heap[0][0]:
        #         heapq.heappushpop(heap, (dist,i))
        # return [points[i] for _, i in (heap) ]
        heap = []
        heapq.heapify(heap)
        for i in range(len(points)):
            heapq.heappush(heap,(self.squarefunc(points[i]), i))
        result = []
        for i in range(k):
            _, idx = heapq.heappop(heap)
            result.append(points[idx])
        return result
            
            
            
            
    
    def squarefunc(self, point):
        return point[0]**2 + point[1]**2