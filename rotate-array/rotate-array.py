class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # [1,2,3,4,5,6,7]
        # [0,1,2,3,4,5,6]  len = 7 k=3
#          l     r
        if len(nums) <2:
            return 
        nums.reverse()
        left = 0
        if k > len(nums):
            k = k%len(nums)
        right = k-1
        while left<right:
            nums[left], nums[right] = nums[right], nums[left]
            left+=1
            right-=1
        
        left = k
        right = len(nums)-1
        if k > len(nums):
            k = k%len(nums)
        while left<right:
            nums[left], nums[right] = nums[right], nums[left]
            left+=1
            right-=1

        