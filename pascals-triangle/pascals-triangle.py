class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        if numRows > 0:
            res.append([1])
        if numRows > 1:
            res.append([1,1])
        prev = [1,1]
        while numRows>2:
            curr = [1]
            for i in range(len(prev)):
                if i < len(prev) and i+1 < len(prev):
                    curr.append(prev[i]+prev[i+1])
                else:
                    break
            curr.append(1)
            res.append(curr)
            prev = curr
            numRows-=1
        return res
            