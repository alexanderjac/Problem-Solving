class Solution:
    def posLeft(self,arr, target,low, high ):
        # if low ==0 and arr[low]>target:
        #     return 0
        while low<  high :
            mid = low + (high- low)//2
            # if  arr[mid-1]<target and arr[mid]>=target:
            #     return mid 
            if arr[mid] >= target:
                high = mid  
            else:
                low = mid +1
            
#         for i in range(low,high):
#             if arr[i]>= target:
#                 return i 
        return low  
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        result = 0
        for i in range(len(nums)):
            num = nums[i]
            result += bisect_right(nums, upper-num, i+1, len(nums))  - self.posLeft(nums, lower-num, i+1, len(nums))
        
        return result
        nums.sort()
        ans=0
        for i in range(len(nums)-1, -1, -1):
            v = nums[i]
            a = bisect_left(nums, lower - v, lo=0, hi=i)
            b = bisect_right(nums, upper - v, lo=0, hi=i)
            ans += b - a
        return ans 
#         ans = 0
#         nums.sort()
#         for idx, num in enumerate(nums):
#             low  = idx+1
#             high = len(nums) 
#             while low<high:
#                 mid = low + (high -low)//2
#                 if nums[mid]+ num>=lower:
#                     high = mid
#                 else:
#                     low = mid+1
#             lbound = low
#             low = idx +1
#             high = len(nums) 
#             while low<high:
#                 mid = low +(high-low)//2
#                 if nums[mid] + num> upper:
#                     high = mid
#                 else:
#                     low = mid +1
#             rbound = low -1
#             ans += rbound - lbound +1

#         return ans