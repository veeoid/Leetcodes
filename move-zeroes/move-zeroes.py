class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        curr = -1
        
        for i in range(len(nums)-1):
            k = i+1
            curr = nums[i]
            if nums[i] == 0:
                while k < len(nums)-1 and nums[k]==0:
                    k+=1
                nums[i]=nums[k]
                nums[k]=curr
                