class Solution:
    def interpret(self, command: str) -> str:
        ans = [0]*3
        i = 0
        ans[i] = command
        if "()" in command:
            i += 1
            ans[i] = command.replace("()","o")
        if "(al)" in command:
            i += 1
            ans[i] = ans[i-1].replace("(al)","al")
        return ans[i]
