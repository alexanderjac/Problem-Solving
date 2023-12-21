class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        seen = set()
        def helper(curr):
            if len(curr) > n:
                return
            if len(curr)==n:
                res.append(curr.copy())
                return 
            for i in range(n):
                print("nums[i]: ", nums[i])
                print("seen: ",  seen)
                if nums[i] in seen:
                    continue
                ele = nums[i]
                seen.add(ele)
                helper(curr+[ele])
                seen.remove(ele)
            return 
        helper([])
        return res
        