class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        check = True
        for r in range(len(matrix)):
            i = r
            j = 0
            ch = matrix[i][j]
            while(i<len(matrix) and j<len(matrix[0])):
                if ch != matrix[i][j]:
                    check = False
                    return check
                i += 1
                j += 1
        for c in range (1,len(matrix[0])):
            i = 0
            j = c
            ch = matrix[i][j]
            while(j<len(matrix[0]) and i<len(matrix)):
                if ch != matrix[i][j]:
                    check = False
                    return check
                i += 1
                j += 1
        return check
