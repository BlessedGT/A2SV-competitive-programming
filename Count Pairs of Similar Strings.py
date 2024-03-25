class Solution:
    def similarPairs(self, words: List[str]) -> int:
        c = 0
        for i in range(len(words)):
            c1 = {}
            for e in words[i]:
                c1[e] = c1.get(e,0) + 1
            for j in range(i+1,len(words)):
                c2 = {}
                for el in words[j]:
                    c2[el] = c2.get(el,0) + 1
                if c2.keys() == c1.keys():
                    c+=1
        return c
