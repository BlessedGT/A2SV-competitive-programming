class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        ans = [0]*len(nums)
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i], nums[i+1] = 2*nums[i], 0
        j=0
        for nm in nums:
            if nm != 0:
                ans[j] = nm
                j += 1
        return ans
