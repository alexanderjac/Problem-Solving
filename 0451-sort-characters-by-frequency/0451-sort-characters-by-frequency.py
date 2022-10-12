class Solution:
    def frequencySort(self, s: str) -> str:
        
        """
        abbcddddd
        {
        a:1
        c:1
        d:5
        }
        
        heap = 
        [(a, 1)]
        """
        heap  = []
        heapq.heapify(heap)
        freq ={}
        for i in range(len(s)):
            freq[s[i]] = freq.get(s[i], 0) +1
        for key in freq.keys():
            heapq.heappush(heap, ( -freq[key], key))
        
        result =""
        while heap:
            frequency, ele = heapq.heappop(heap)
            frequency = frequency*-1
            for i in range(frequency):
                result +=ele
        return result
            
            