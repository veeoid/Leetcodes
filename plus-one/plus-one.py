class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        sm = ''
        for i in digits:
            sm+=str(i)
        
        sm = str(int(sm)+1)
        d = [int(x) for x in sm]
        print(d)
        return d