class Solution:
    def compress(self, chars: List[str]) -> int:
        start = 0
        end = 1
        count = 1
        while end < len(chars):
            if chars[start] != chars[end]:
                if count > 1:
                    for i in list(str(count)):
                        chars.insert(end, i)
                        end+=1
                start = end
                end += 1
                count = 1
            elif chars[start] == chars[end]:
                chars.pop(end)
                count += 1
        if count > 1:
            for i in list(str(count)):
                chars.insert(end, i)
                end+=1
                

