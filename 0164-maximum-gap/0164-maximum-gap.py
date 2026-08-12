class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums.sort()
        maximum = 0
        for i in range(len(nums)-1):
            new = nums[i+1] - nums[i]
            maximum = max(new,maximum)
        return maximum