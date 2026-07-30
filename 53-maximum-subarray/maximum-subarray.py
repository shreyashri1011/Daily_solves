class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp=[0]*len(nums)
        for i ,n in enumerate(nums):
            dp[i]=max(n,dp[i-1]+n)
        return max(dp)