class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1 for i in range(len(nums))]
        forward_carry = 1
        for i in range(0, len(nums)-1):
            forward_carry*= nums[i]
            result[i+1] *= forward_carry
        backward_carry = 1
        for i in reversed(range(1, len(nums))):
            backward_carry*= nums[i]
            print(backward_carry)
            result[i-1] *= backward_carry
        return result