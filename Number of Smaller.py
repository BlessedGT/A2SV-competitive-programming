a,b = map(int, input().split())
arr1 = [int(x) for x in input().split()]
arr2 = [int(x) for x in input().split()]

smaller = []
j = 0
for i in range(len(arr2)):
    while j < len(arr1) and arr1[j] < arr2[i]:
        j += 1
    smaller.append(j)
print(" ".join(str(x) for x in smaller))
