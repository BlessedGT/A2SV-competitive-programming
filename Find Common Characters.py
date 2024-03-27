class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        ans = []
        ch = {}
        for i in words[0]:
            ch[i] = ch.get(i,0) + 1
          
        for j in ch:
            mn = ch[j]
            for k in range(1,len(words)):
                mn = min(mn , words[k].count(j))
            ans.extend(mn*j)
        return ans
