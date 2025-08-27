class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        myDict = defaultdict(int)
        counter = 0
        for i in nums:
            if myDict[i] > 0:
                counter += 1
                myDict[i] -= 1
            else:
                myDict[k - i] += 1
        return counter