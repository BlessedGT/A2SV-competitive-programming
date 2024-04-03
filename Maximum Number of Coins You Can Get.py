class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        c = 0
        turn = 2*(len(piles)//3)
        piles = sorted(piles, reverse = True)
        
        for i in range(1,turn,2):
            c += piles[i]
        return c
