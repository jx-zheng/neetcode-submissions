import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canFinishEating(k) -> bool:
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / k)
            
            return hours <= h

        max_pile_size = max(piles)

        l, r = 1, max_pile_size
        mid = 1
        while l < r:
            mid = (l + r) // 2
            if canFinishEating(mid):
                r = mid
            else:
                l = mid + 1
        
        return r
