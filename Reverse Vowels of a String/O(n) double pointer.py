class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")
        chars = list(s)
        head = 0
        tail = len(s) - 1
        while head < tail:
            while head < tail and chars[head] not in vowels:
                head+=1
        
            while head < tail and chars[tail] not in vowels:
                tail-=1

            if chars[head] in vowels and chars[tail] in vowels:
                temp = chars[head]
                chars[head] = chars[tail]
                chars[tail] = temp
                head+=1
                tail-=1
        return "".join(chars)
                
                