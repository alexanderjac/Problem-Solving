class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        presum = [0 for i in range(n)]
        for start, end, value in bookings:
            presum[start-1] += value
            if end<n:
                presum[end] -= value
        for i in range(1,n):
            presum[i] += presum[i-1]
        return presum
        # res = [0 for i in range]
        
        
        """
        hashMap = {}
        for booking in bookings:
            first = booking[0]
            second = booking[1]
            seat = booking[2]
            for i in range(first, second+1):
                if i in hashMap:
                    hashMap[i] += seat
                else:
                    hashMap[i] = seat
            # if first in hashMap:
            #     hashMap[first] += seat
            # else:
            #     hashMap[first] = seat
            # if second in hashMap:
            #     hashMap[second] += seat
            # else:
            #     hashMap[second] = seat
        result = []
        for i in range(1,n+1):
            if i in hashMap:
                result.append(hashMap[i])
            else:
                result.append(0)
        return result
        """