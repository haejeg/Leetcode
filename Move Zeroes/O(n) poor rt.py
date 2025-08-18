class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        arrLength = len(nums)
        i = 0
        zeroCount = 0
        while i < arrLength:
            print("i", i)
            if nums[i] == 0:
                nums.pop(i)
                zeroCount+=1
                arrLength -= 1
            else:
                i+=1
            
        for i in range(0, zeroCount):
            nums.append(0)