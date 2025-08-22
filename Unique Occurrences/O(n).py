class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        newDict = {}
        for i in arr:
            if i not in newDict:
                newDict[i] = 1
            else:
                newDict[i] += 1

        anotherDict = {}
        for key,values in newDict.items():
            if values not in anotherDict:
                anotherDict[values] = 1
            else:
                return False

        print(newDict)
        return True
        