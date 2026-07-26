class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        new=[]
        for i in nums:
            new.append(i*i)
        return sorted((new))