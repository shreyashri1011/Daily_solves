class Solution(object):
    def timeRequiredToBuy(self, tickets, k):
        """
        :type tickets: List[int]
        :type k: int
        :rtype: int
        """
        result=0
        for i in range(len(tickets)):
            if i<=k:
                result+=min(tickets[i],tickets[k])
            else:
                result+=min(tickets[i],tickets[k]-1)
        return result
            