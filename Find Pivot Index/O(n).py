class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        arrLength = len(nums)
        newArray = [0] * arrLength
        sum = 0
        for i in range(1, arrLength): 
            sum += nums[i - 1]
            newArray[i] = sum

        sum = 0
        for i in range(arrLength - 2, -1, -1):
            sum -= nums[i + 1]
            newArray[i] += sum

        for i in range(0, arrLength):
            if newArray[i] == 0:
                return i
        return -1