# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0\


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        l = len(nums)
        new_list=[]
        for i in range(l-2):
            if(i!=0 and nums[i]==nums[i-1]): continue
            low = i+1
            high = l-1
            while(low<high):
                sum3=nums[i]+nums[low]+nums[high]
                if (sum3==0):
                    new_list.append([nums[i],nums[low],nums[high]])
                    # low+=1
                    # high-=1
                    while (low<high and nums[low]==nums[low+1]):
                        low+=1
                    while low<high and nums[high]==nums[high-1]:
                        high-=1
                    low+=1
                    high-=1
                elif(sum3>0):
                    high-=1
                else:
                    low+=1
        return new_list