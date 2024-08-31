from heapq import heappop, heappush, heapify

class Solution:
    #Function to return the minimum cost of connecting the ropes.
    def minCost(self, arr) -> int:
        heap, res = list(), list()
        heapify(arr)
        while len(arr) >= 2:
            cost = heappop(arr)+heappop(arr)
            heappush(arr, cost)
            res.append(cost)
        
        return sum(res)
