# TC: O(n)
# SC: O(n)
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        cumulative_sum =0
        cumulative_freq = {}
        cumulative_freq[0] =1
        for i in range(len(nums)):
            cumulative_sum += nums[i]
            if (cumulative_sum - k) in cumulative_freq:
                count += cumulative_freq[cumulative_sum - k]
            cumulative_freq[cumulative_sum] = 1 + cumulative_freq.get(cumulative_sum,0)
        return count

# First Approach

# TC: O(n^2)
# SC: O(1)
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        count =0
        cumulative_sum = [0 for i in range(len(nums)+1)]
        for i in range(1, len(nums)+1):
            cumulative_sum[i] =cumulative_sum[i-1] +nums[i-1]
        for i in range(len(cumulative_sum)-1):
            for j in range(i+1,len(cumulative_sum)):
                if cumulative_sum[j] - cumulative_sum[i] == k:
                          count+=1
        return count
