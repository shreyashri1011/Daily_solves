class Solution(object):
    def concatWithReverse(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        temp=[0]*n
        for i in range(n):
            temp[i]=nums[n - i - 1]
        return nums+temp