class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        start = 0
        next = 1
        end = len(nums) - 1
        while start < end:
            if nums[start] == 0 and nums[end] != 0:
                temp = nums[start]
                nums[start] = nums[end]
                nums[end] = temp
            else:
                start+=1
            if end == 0:
                end-=1
        