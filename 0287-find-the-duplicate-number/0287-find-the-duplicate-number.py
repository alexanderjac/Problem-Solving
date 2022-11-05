class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        low = 1
        high = len(nums) -1
        while low <=high:
            curr = low +(high-low)//2
            count = 0
            count = sum(  num<=curr for num in nums)
            if count>curr:
                duplicate = curr
                high = curr -1
            else:
                low = curr+1
        return duplicate
        
        # for i in range(len(nums)):
        #     index = abs(nums[i]) 
        #     if nums[index]<0:
        #         return abs(nums[i])
        #     nums[index]  = -nums[index]
            
        