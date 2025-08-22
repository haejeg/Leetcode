class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        start = 0
        end = 1
        length = len(nums)
        while end < length and start < (length - 1):
            if nums[start] == 0 and nums[end] != 0:
                temp = nums[start]
                nums[start] = nums[end]
                nums[end] = temp
                start+=1
                end+=1
            elif nums[start] == 0 and nums[end] == 0:
                end+=1
            elif nums[start] != 0:
                start+=1
                end+=1