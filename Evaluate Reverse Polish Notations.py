class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        ops = "+-/*"
        for t in tokens:
            if t in ops:
                a,b = stk.pop(),stk.pop()
                if t == "+":
                    stk.append(b+a)
                elif t == "-":
                    stk.append(b-a)
                elif t == "*":
                    stk.append(b*a)
                elif t == "/":
                    stk.append(int(b/a))
            else:
                stk.append(int(t))
        return stk[0]
