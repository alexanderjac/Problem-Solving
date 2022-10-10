class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for n in nums:
            # n^0 = n doing xor with anynumber and zero would be that number
            res = res^n
        return res
        