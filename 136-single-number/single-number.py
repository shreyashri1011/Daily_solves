class Solution(object):
    def singleNumber(self, nums):
        xor=0
        for i in nums:
            xor^=i
        return xor