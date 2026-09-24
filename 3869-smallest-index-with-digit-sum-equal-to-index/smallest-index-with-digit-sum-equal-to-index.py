class Solution(object):
    def smallestIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i, n in enumerate(nums):
            total = sum(int(c) for c in str(n))
            if total == i:
                return i
        return -1