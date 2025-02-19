class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # edge case: str1[0] and str2[0] are not the sample
        # multiply string splits and if string isn't reproduceable, reduce divisible size
        finalstr = ""
        len2 = len(str2)
        len1 = len(str1)
        for i in range(len(str1)):
            print(i)
            if i > len2:
                break
            if (str1[0: i + 1] * int(len1 / len(str1[0: i + 1]))) == str1 and (str2[0: i + 1] * int(len2 / len(str2[0: i + 1])) == str2) and str1[0: i + 1] == str2[0: i + 1]:
                print("Recgonized: ", i + 1, str1[0:i + 1], str2[0: i + 1])
                finalstr = str1[0:i + 1]

        return finalstr