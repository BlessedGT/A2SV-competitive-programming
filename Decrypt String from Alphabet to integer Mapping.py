class Solution:
    def freqAlphabets(self, s: str) -> str:
        ans = []
        i = len(s) - 1
        while(i>=0):
            if s[i] == '#':
                x = int(s[i-2]+s[i-1])-10
                ans.append(chr(ord('j') + x))
                i -= 3
            else:
                x = int(s[i])-1
                ans.append(chr(ord('a') + x))
                i -= 1
        return ("".join(ans[::-1]))
