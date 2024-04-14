class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        l = 0
        ans = []
        for r in spaces:
            ans.append(s[l:r])
            l = r
        ans.append(s[l:len(s)])
        return " ".join(ans)
