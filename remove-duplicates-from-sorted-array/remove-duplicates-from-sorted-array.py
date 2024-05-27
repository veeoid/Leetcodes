class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        prev = None
        count = 0
        while i < len(nums):
            if prev == nums[i]:
                nums.pop(i)
            else:
                prev = nums[i]
                i+=1
                count+=1
        return count
                
            
            
            
            