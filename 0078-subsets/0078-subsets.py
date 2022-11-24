class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.helper(nums,0, res, [])
        return res
    def helper(self, nums, idx, res,curr):
        res.append(curr.copy())
        for i in range(idx, len(nums)):
            self.helper(nums, i+1, res,curr +[nums[i]])
        