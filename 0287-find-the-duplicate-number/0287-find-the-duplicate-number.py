class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            # print(nums)
            index = abs(nums[i]) 
            if nums[index]<0:
                return abs(nums[i])
            nums[index]  = -nums[index]
            
        