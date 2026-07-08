class Solution:
    def twoSum(self,nums,target):
        hash = {}

        for i in range(len(nums)):
            need = target - nums[i]
            if need in hash:
                return [hash[need],i]
            hash[nums[i]] = i
            