t = int(input())
for _ in range(t):
    n = int(input())
    nums = [int(x) for x in input().split()]
    
    sm = 0
    l, r = 0, 1
    while r < n:
        if nums[l] * nums[r] < 0:
            sm += max(nums[l:r])
            l = r
        r += 1
    
    sm += max(nums[l:r])
    print(sm)
