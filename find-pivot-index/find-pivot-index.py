class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        left_sum = 0 
        i=0
        while i < len(nums):
            right_sum = total_sum - left_sum - nums[i]
            if right_sum == left_sum:
                return i
            left_sum+=nums[i]
            i+=1
        return -1