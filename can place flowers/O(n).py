class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        newlist = []
        # print(len(flowerbed))
        if len(flowerbed) == 1:
            if flowerbed[0] == 0:
                return 1 >= n
            else:
                return 0 >= n


        for i in range(len(flowerbed)):
            if i == 0:
                if flowerbed[i+1] == 0 and flowerbed[i] == 0:
                    newlist.append(i)
            elif i == len(flowerbed) - 1:
                if flowerbed[i-1] == 0 and flowerbed[i] == 0:
                    newlist.append(i)
            elif flowerbed[i-1] == 0 and flowerbed[i+1] == 0 and flowerbed[i] == 0:
                newlist.append(i)
            # print(newlist)

        if len(newlist) <= 1:
            return len(newlist) >= n

        i = 0
        while i < len(newlist) - 1:
            if newlist[i + 1] - newlist[i] <= 1:
                del newlist[i + 1]  # Remove adjacent element
            else:
                i += 1  # Move to the next element only when no deletion occurs

        # print(newlist)
        return len(newlist) >= n