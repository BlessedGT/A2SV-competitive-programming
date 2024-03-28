class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        ans = []
        for y in range(len(grid)-2):
            mxrow = []
            for x in range(len(grid[0])-2):
                mx = float("-inf")
                for i in range(3):
                    for j in range(3):
                        mx = max(mx,grid[y+i][x+j])
                mxrow.append(mx)
            ans.append(mxrow)
        return ans
