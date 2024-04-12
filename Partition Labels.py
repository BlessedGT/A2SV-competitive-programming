class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        occ = {}
        for i,ch in enumerate(s):
            occ[ch] = i

        mx = mn = 0
        ans = []
        for i,ch in enumerate(s):
            mx = max(mx,occ[ch])
            if i == mx:
                mx = mx-mn + 1
                ans.append(mx)
                mn = i + 1
        return ans
