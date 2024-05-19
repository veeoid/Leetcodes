class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        rows = len(matrix)
        cols = len(matrix[0])
        curr_col = curr_row = 0
        while cols > 0 and rows > 0:
            for i in range(cols):
                res.append(matrix[curr_row][curr_col])
                curr_col += 1
            curr_col -= 1
            rows -= 1
            curr_row += 1

            if rows == 0 or cols == 0:
                break

            for i in range(rows):
                res.append(matrix[curr_row][curr_col])
                curr_row += 1
            curr_row -= 1
            curr_col -= 1
            cols -= 1

            if rows == 0 or cols == 0:
                break

            for i in range(cols):
                res.append(matrix[curr_row][curr_col])
                curr_col -= 1
            curr_col += 1
            curr_row -= 1
            rows -= 1

            if rows == 0 or cols == 0:
                break

            for i in range(rows):
                res.append(matrix[curr_row][curr_col])
                curr_row -= 1
            curr_row+=1
            curr_col += 1
            cols -= 1

            if rows == 0 or cols == 0:
                break

        return res
