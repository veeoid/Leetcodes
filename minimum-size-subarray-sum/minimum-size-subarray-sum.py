class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        right = 0
        curr_sum = 0
        curr_min = float('inf')
        
        while right < len(nums):
            curr_sum += nums[right]
            while curr_sum >= target:
                curr_min = min(curr_min, right - left + 1)
                curr_sum -= nums[left]
                left += 1
            right += 1
        
        return 0 if curr_min == float('inf') else curr_min
                
# [2,3,1,2,4,3] t = 7
#  l 
#  r
# 