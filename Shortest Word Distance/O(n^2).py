class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        newArr = []
        words = [word1, word2]
        for i in range(0, len(wordsDict)):
            if wordsDict[i] in words:
                words.remove(wordsDict[i])
                for j in range(i + 1, len(wordsDict)):
                    if wordsDict[j] in words:
                        newArr.append(j - i)
                        words.remove(wordsDict[j])
                        words.append(word1)
                        words.append(word2)
        print(newArr)
        return min(newArr)