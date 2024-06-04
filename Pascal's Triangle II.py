class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex < 2:
            return [1]*(rowIndex+1)
        
        ans = [1]
        for _ in range(1,rowIndex+1):
            ans.append(1)
            for j in range(len(ans)-2,0,-1):
                ans[j] = ans[j] + ans[j-1]
        return ans
