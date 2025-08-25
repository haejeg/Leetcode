class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rowDict = defaultdict(int)
        colDict = defaultdict(int)
        total = 0
        for i in range(0, len(grid)):
            row = tuple(grid[i])
            column = tuple([row[i] for row in grid])
            rowDict[row] += 1
            colDict[column] += 1

        for i, j in rowDict.items():
            if i in colDict:
                total += j * colDict[i]
                
        return total