class Solution:
    def simplifyPath(self, path: str) -> str:
        ans = []
        path = path.split('/')
        
        for itm in path:
            if itm == '..':
                if ans:
                    ans.pop()
            elif itm == '' or itm == '.':
                continue
            else:
                ans.append(itm)
        
        return '/'+'/'.join(ans)
