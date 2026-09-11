import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # (freq, number)
        nums_count = Counter(nums)
        counted_items = list(nums_count.items())
        for i in range(len(counted_items)):
            counted_item = counted_items[i]
            counted_items[i] = (-counted_item[1], counted_item[0])
        
        heapq.heapify(counted_items)
        ret = []
        for _ in range(k):
            ret.append(heapq.heappop(counted_items)[1])

        return ret
