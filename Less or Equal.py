n,l= map(int, input().split())
arr = [int(x) for x in input().split()]
arr.sort()
if l == 0 and (arr[0]-1)>=1:
    print(arr[0]-1)
elif (l<n and arr[l] != arr[l-1] and l!=0):
    print(arr[l-1]) 
elif (l==n):
    print(arr[l-1])
else:
    print(-1)
