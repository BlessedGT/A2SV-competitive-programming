class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        mxsm = csm = sum(nums[:k])
        l = 0
        r = k
        while(r<len(nums)):
            csm = (csm - nums[l]) + nums[r]
            mxsm = max(mxsm,csm)
            l += 1
            r += 1
        return mxsm/k
