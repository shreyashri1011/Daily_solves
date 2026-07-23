class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap={}
        for i,v in enumerate(nums):
            diff=target-v
            if diff in hashmap:
                return [i,hashmap[diff]]
            hashmap[v]=i