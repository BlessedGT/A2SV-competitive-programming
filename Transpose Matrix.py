class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        trn = []
        for c in range(len(matrix[0])):
            tmp = []
            for r in matrix:
                tmp.append(r[c])
            trn.append(tmp)
        return trn
