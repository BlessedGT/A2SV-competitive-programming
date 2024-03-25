class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        s = len(nums)
        for i in range(2*s):
            ans.append(nums[i%s])
        return ans
