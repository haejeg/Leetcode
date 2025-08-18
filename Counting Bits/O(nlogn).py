class Solution:
    def countBits(self, n: int) -> List[int]:
        newArray = []
        count = 0
        i = 0
        while i <= n:
            count = 0
            print(i)
            p = i
            while p > 0:
                p = p & (p - 1)
                count+=1
            newArray.append(count)
            i+=1
        print(newArray)
        return newArray