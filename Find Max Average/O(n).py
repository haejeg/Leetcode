class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        averageArrays = []
        sum_k = sum(nums[0 : k])
        averageArrays.append(sum_k / k)
        for i in range(1, len(nums) - k + 1):
            # print(i)
            sum_k -= nums[i - 1]
            sum_k += nums[i + k - 1]
            averageArrays.append(sum_k / k)
        # print(averageArrays)
        return max(averageArrays)