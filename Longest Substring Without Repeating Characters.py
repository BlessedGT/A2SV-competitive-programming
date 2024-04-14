class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        l,r = 0,1
        ans = 0
        while r<len(s):
            while s[r] in s[l:r] and r-l>0:
                l += 1
            ans = max(ans,r-l+1)
            r+=1
        return ans
