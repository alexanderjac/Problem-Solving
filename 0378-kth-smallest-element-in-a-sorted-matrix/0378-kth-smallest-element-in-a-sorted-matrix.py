class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = []
        n = len(matrix)
        for i in range(min(k, n)):
            heapq.heappush(heap, (matrix[i][0], i,0))
        heapq.heapify(heap)

        while k :
            ele, r , c = heapq.heappop(heap)
            if c<n-1:
                heapq.heappush(heap, (matrix[r][c+1], r, c+1))
            k -=1
        return ele