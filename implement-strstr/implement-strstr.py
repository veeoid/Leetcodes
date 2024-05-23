class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack) < len(needle):
            return -1
        i = 0
        for x in range(len(haystack)):
            while needle[i] == haystack[x]:
                if i == len(needle) - 1:
                    return x - i
                i+=1
                x+=1
                if x > len(haystack)-1:
                    break
            i = 0
            
        return -1