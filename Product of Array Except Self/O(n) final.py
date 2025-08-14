class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # pre should be [1, 1, 2, 6]
        arrayLength = len(nums)
        productArray = [1] * arrayLength
        prefix = 1
        for i in range(0, arrayLength):
            productArray[i] = prefix
            prefix *= nums[i]

        # post should be [24, 12, 4, 1]
        postfix = 1
        for i in range(arrayLength - 1, -1, -1):
            productArray[i] *= postfix
            postfix *= nums[i]
        return productArray
        