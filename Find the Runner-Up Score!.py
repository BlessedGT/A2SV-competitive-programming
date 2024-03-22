if __name__ == '__main__':
    n = int(input())
    arr = [int(x) for x in input().split()]
    
    arr.sort()
    for i in range(n-1,0,-1):
        if int(arr[i]) > int(arr[i-1]):
            print(arr[i-1])
            break
