class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        lowest = float('inf')
        second_lowest = float('inf')
        for i in nums:
            if i <= lowest:
                lowest = i
            elif i <= second_lowest:
                second_lowest = i
            else:
                return True
        return False