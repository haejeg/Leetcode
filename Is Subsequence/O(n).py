class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        list_t = list(t)
        list_s = list(s)
        len_t = len(list_t)
        len_s = len(list_s)
        i = 0
        j = 0
        newArray = []
        while i < len_s and j < len_t:
            if list_s[i] != list_t[j]:
                j+=1
            elif list_s[i] == list_t[j]:
                print(list_s[i])
                newArray.append(list_s[i])
                j+=1
                i+=1
        return newArray == list_s
