class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        # nums.sort()
        res = 0
        n = len(nums)
        for i in range(n):
            minvalue =  math.inf
            maxvalue = -math.inf
            for j in range(i,n):
                minvalue = min(nums[j], minvalue)
                maxvalue = max(nums[j],maxvalue)
                res += maxvalue - minvalue
        return res

    """
    
    
    class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        n = len(nums)
        answer = 0
        
        for left in range(n):
            min_val, max_val = math.inf, -math.inf
            for right in range(left, n):
                max_val = max(max_val, nums[right])
                min_val = min(min_val, nums[right])
                answer += max_val - min_val
                
        return answer
    """