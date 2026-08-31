class Solution(object):

    def findCheapestPrice(self, n, flights, src, dst, k):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type k: int
        :rtype: int
        """

        prices = [float("inf")] * n

        prices[src] = 0

        for i in range(k + 1):

            tmpPrices = prices[:]

            for from_node, to_node, cost in flights:

                if prices[from_node] == float("inf"):
                    continue

                if prices[from_node] + cost < tmpPrices[to_node]:
                    tmpPrices[to_node] = prices[from_node] + cost

            prices = tmpPrices

        if prices[dst] == float("inf"):
            return -1

        return prices[dst]