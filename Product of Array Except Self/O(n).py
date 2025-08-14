class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # pre should be [1, 1, 2, 6]
        arrayLength = len(nums)
        productArray = [1] * arrayLength
        for i in range(1, arrayLength):
            productArray[i] *= nums[i - 1]
            productArray[i] *= productArray[i - 1]
        print(productArray)

        #post should be [24, 12, 4, 1]
        postArray = [1] * arrayLength
        numsReversed = nums[::-1]
        print(numsReversed)
        for i in range(len(nums) - 2, -1, -1):
            postArray[i] *= nums[i + 1]
            postArray[i] *= postArray[i + 1]
        print(postArray)

        