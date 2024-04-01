#User function Template for python3

class Solution: 

    def selectionSort(self, arr,n):
        for i in range(n):
            mnx = i
            for j in range(i,n):
                if arr[mnx] > arr[j]:
                    mnx = j
            arr[i],arr[mnx] = arr[mnx], arr[i]
        return arr
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().selectionSort(arr, n)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends
