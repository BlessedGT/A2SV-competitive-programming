class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        ans = 0
        l = 0
        o = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                o += 1
            while o>k:
                if nums[l] == 0:
                    o -= 1
                l += 1
            ans = max(r-l+1,ans)
        return ans
