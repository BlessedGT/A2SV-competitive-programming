class Solution:
    def isValid(self, s: str) -> bool:
        check = {'(':')','[':']','{':'}'}

        stk = []
        l = len(s)-1

        for i in range(l,-1,-1):
            curr_br = s[i]
            if curr_br in check.keys():
                if stk and stk[-1] == check[curr_br]:
                    stk.pop()
                else:
                    return False
            else:
                stk.append(curr_br)
                
        return not stk
