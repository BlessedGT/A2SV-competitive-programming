class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        lsr = {}
        for w,l in matches:
            lsr[l] = lsr.get(l, 0) + 1
            
        wnr = {m[0] for m in matches}

        winners = [i for i in wnr if i not in lsr]
        losers = [j for j in lsr if lsr[j] == 1]

        winners.sort()
        losers.sort()

        return [winners,losers]
