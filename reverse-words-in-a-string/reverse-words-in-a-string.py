class Solution:
    def reverseWords(self, s: str) -> str:
        s_list = s.split()
        s_list.reverse()
        s = ""
        for i in s_list:
            if s == "":
                s+=i
            else:
                s+= " "+i
        return s