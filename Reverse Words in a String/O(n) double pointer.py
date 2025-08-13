class Solution:
    def reverseWords(self, s: str) -> str:
        chars = list(s)
        words =  s.split()
        head = 0
        tail = len(words) - 1
        while head < tail:
            temp = words[head]
            words[head] = words[tail]
            words[tail] = temp
            head+=1
            tail-=1
        return " ".join(words)
            
        