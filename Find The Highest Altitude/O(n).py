class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        biggestGain = 0
        elevation = 0
        for i in gain:
            elevation += i
            if biggestGain <= elevation:
                biggestGain = elevation
        return biggestGain