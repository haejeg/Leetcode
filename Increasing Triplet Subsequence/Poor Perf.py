class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False

        lowest_idx = 0
        second_lowest_idx = None
        i = 0
        while i < len(nums):
            if not second_lowest_idx and nums[i] > nums[lowest_idx]:
                second_lowest_idx = i
            if nums[i] < nums[lowest_idx]:
                lowest_idx = i
            if nums[i] > nums[lowest_idx] and nums[i] < nums[second_lowest_idx]:
                second_lowest_idx = i
            if second_lowest_idx and nums[i] > nums[second_lowest_idx]:
                return True
            i += 1
        return False