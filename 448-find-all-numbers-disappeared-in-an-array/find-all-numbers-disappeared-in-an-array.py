class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        seen=set(nums)
        ret=[]
        for i in range (1,len(nums)+1):
            if i not in seen:
                ret.append(i)
        return ret