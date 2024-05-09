class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        nums_dict = {}
        for i in range(len(nums)):
            nums_dict[nums[i]] = i

        nums.sort()
        if nums[-1] >= nums[-2] * 2:
            return nums_dict[nums[-1]]
        return -1