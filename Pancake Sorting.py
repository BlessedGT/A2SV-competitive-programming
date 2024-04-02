class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
      
        def flip(k):
            ans.append(k+1)
            i = 0
            while(i<k):
                arr[i], arr[k] = arr[k], arr[i]
                i += 1
                k -= 1
              
        ans = []  
        l = len(arr)
        for i in range(l-1,-1,-1):
            mx = i
            for j in range(i, -1, -1):
                if arr[j] > arr[mx]:
                    mx = j
            if mx != i:
                flip(mx)
                flip(i)
        return ans
