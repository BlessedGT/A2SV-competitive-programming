n = int(input())
ans = []
for i in range(n):
    l = int(input())
    arr = [int(x) for x in input().split()]
    
    if l == 1:
        ans.append("YES")
    else:
        arr.sort()
        c = True
        
        for i in range(l-1):
            if (arr[i+1] - arr[i]) > 1:
                ans.append("NO")
                c = False
                break
        if c == True:
            ans.append("YES")
                
for itm in ans:
    print(itm)
