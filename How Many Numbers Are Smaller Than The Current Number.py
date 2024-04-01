class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ns = sorted(nums)
        ans = []
        for i in nums:
            ans.append(ns.index(i))
        return ans
