class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        arrLength = len(nums)
        newArray = [0] * arrLength
        sum = 0
        for i in range(1, arrLength): 
            sum += nums[i - 1]
            newArray[i] = sum

        sum = 0
        j = -1
        if newArray[arrLength - 1] == 0:
            j = arrLength - 1

        for i in range(arrLength - 2, -1, -1):
            sum -= nums[i + 1]
            newArray[i] += sum
            if newArray[i] == 0:
                j = i
        return j