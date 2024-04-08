class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "AaEeIiOoUu"
        st = [a for a in s]
        l,r = 0,len(st)-1
        while l<r:
            if (st[l] in vowels) and (st[r] in vowels):
                st[l],st[r] = st[r],st[l]
                l += 1
                r -= 1
            elif st[l] not in vowels:
                l += 1
            elif st[r] not in vowels:
                r -= 1
        return "".join(st)
