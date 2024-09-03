# required time: O(n.log(k))
# time limit exceeded

from heapq import heappush, heappop

class Solution:
    def nearlySorted(self,a,n,k):
        res, heap = list(), list()
        while a:
            item = a.pop(0)
            heappush(heap, item)
            if k == 0:
                res.append(heappop(heap))
                k += 1
            k -= 1
        while heap:
            res.append(heappop(heap))
        return res
