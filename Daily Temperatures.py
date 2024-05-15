class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0]*len(temperatures)
        stk = []

        for i in range (len(temperatures)):
            while stk and temperatures[stk[-1]] < temperatures[i]:
                ans[stk[-1]] = i - stk[-1]
                stk.pop()
            stk.append(i)
        return ans
                
