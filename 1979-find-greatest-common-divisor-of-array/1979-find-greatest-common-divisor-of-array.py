import math
class Solution:
    def findGCD(self, nums: list[int]) -> int:
        min = nums[0]
        max = nums[0]

        for i in range(len(nums)):
            if nums[i] > max:
                max = nums[i]
            if nums[i] < min:
                min = nums[i]
        while min:
            max , min = min , max % min
        return max
            