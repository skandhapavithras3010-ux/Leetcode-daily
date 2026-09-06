class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = []
        n = 0

        for i in nums:
            n += i
            ans.append(n)
        return ans