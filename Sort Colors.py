class Solution:
    def sortColors(self, nums: List[int]) -> None:
        count = [0]*3
        for i in nums:
            count[i] += 1

        k = 0
        for index, value in enumerate(count):
            for i in range(value):
                nums[k] = index
                k += 1
        return nums
