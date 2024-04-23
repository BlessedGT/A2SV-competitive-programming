class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        k = len(p)
        ans = []
        count = Counter(p)
        res = Counter(s[:k])

        if count == res:
            ans.append(0)
            
        for i in range(k,len(s)):
            res[s[i-k]] -= 1

            if i-k == 0:
                del res[i-k]
                
            res[s[i]] += 1

            if count == res:
                ans.append(i-k+1)
        return ans
