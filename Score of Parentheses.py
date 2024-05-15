class Solution:
    def scoreOfParentheses(self, s: str) -> int:
            stk = [0]
            res = 0

            for p in s:
                if p == '(':
                    stk.append(0)
                else:
                    pp = stk.pop()
                    if pp == 0:
                        stk[-1] += 1
                    else:
                        stk[-1] += 2*pp

            return stk[0]
