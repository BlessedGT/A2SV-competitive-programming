class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        ans = []
        w1 = w2 = 0
        while w1<len(word1) and w2<len(word2):
            if word1[w1:] >= word2[w2:]:
                ans.append(word1[w1])
                w1 += 1
            else:
                ans.append(word2[w2])
                w2 += 1
        return ''.join(ans)+ word1[w1:]+ word2[w2:]
