class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        rev=0
        if x<0:
            sign=-1
        else:
            sign=1
        x=abs(x)
        while x>0:
            rem=x%10
            rev=rev*10+rem
            x=x//10
        rev *= sign
        if rev < -2**31 or rev>2**31-1:
            return 0
        return rev