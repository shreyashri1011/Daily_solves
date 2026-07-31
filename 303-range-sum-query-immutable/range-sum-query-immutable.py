class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.acc_nums=[0]
        for num in nums:
            self.acc_nums.append(self.acc_nums[-1]+num)

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        return self.acc_nums[right+1] - self.acc_nums[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)