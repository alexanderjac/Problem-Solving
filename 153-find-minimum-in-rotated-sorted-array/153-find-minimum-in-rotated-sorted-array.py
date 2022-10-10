class Solution:
    def findMin(self, num):
        first, last = 0, len(num) - 1
        while first < last:
            midpoint = (first + last) // 2
            if num[midpoint] > num[last]:
                first = midpoint + 1
            else:
                last = midpoint
        return num[first]
        