class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        charset = {}
        ans = 0

        for r in range(len(s)):
            charset[s[r]] = charset.get(s[r],0)+1
            while (r-l+1) - max(charset.values()) > k:
                charset[s[l]] -= 1
                l += 1
            ans = max(ans,r-l+1)
            
        return ans
