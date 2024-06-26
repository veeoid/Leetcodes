class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ref_word = strs[0]
        if "" in strs:
            return ""
        for i in strs:
            if len(i) <= len(ref_word):
                ref_word = i
        prefix = 0
        count = 0
        flag = True
        while prefix < len(ref_word):
            for word in strs:
                if ref_word[prefix] != word[prefix] :
                    flag = False
                    break
            if flag == False and count == -1:
                return ""
            count+=1
            if flag == False:
                return ref_word[:prefix:]
            else:
                prefix+=1
            
        return ref_word[:prefix]