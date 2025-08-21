class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        newDict = {}
        for i in nums1:
            if i not in newDict:
                newDict[i] = 1
        print(newDict)

        for j in nums2:
            if j not in newDict:
                newDict[j] = -1
            elif newDict[j] == 1:
                newDict[j] = 0
        print(newDict)

        arr1 = []
        arr2 = []
        for key, value in newDict.items():
            if value <= -1:
                arr2.append(key)
            elif value >= 1:
                arr1.append(key)

        print(arr1)
        print(arr2)
        return arr1, arr2