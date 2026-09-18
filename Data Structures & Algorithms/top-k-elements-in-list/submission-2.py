import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = Counter(nums)

        heap = []
        for num, frequency in frequencies.items():
            heapq.heappush( heap, (frequency, num) )
            if len(heap) > k:
                heapq.heappop(heap)

        ret = [pair[1] for pair in heap]

        return ret
