class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = []
        if rowIndex == 0:
            return [1]
        if rowIndex > 0:
            res.append([1])
            if rowIndex == 1:
                return [1,1]
        if rowIndex > 1:
            res.append([1,1])
        curr_row = 2
        for x in range(2,rowIndex+1):
            prev_row = res[x-1]
            print(x)
            curr = [1]
            for i in range(len(prev_row)-1):
                curr.append(prev_row[i]+prev_row[i+1])
            curr.append(1)
            res.append(curr)
            curr_row+=1
            print(res)
        return res[-1]
                    
            
            
            