class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        reverseOrder = []
        reverseString = ''
        count = 0

        for i in reversed(s):
            if i in vowels:
                reverseOrder.append(i)

        for i in s:
            if i in vowels:
                reverseString += reverseOrder[count]
                count = count + 1
            else:
                reverseString += i
            
        return reverseString